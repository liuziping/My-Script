// 扩展jquery
// 多个ajax执行完毕，出发函数
$.whenAll = function() {
    var lastResolved = 0;

    var wrappedDeferreds = [];

    for (var i = 0; i < arguments.length; i++) {
        wrappedDeferreds.push(jQuery.Deferred());

        arguments[i].always(function() {
            wrappedDeferreds[lastResolved++].resolve(arguments);
        });
    }

    return jQuery.when.apply(jQuery, wrappedDeferreds).promise();
};
// 工具函数 提交
// 传入form的id，成功函数
$.rajax = function(form, fn, data) {
        var $form = $('#' + form)
        var url = $form.attr('action')
        var formstr = $form.serialize()
        if (data) {
            $.each(data, function(k, v) {
                formstr += "&" + k + "=" + v
            })
        };
        $.ajax({
            url: url,
            data: formstr,
            type: 'post',
            dataType: 'json',
            error: function(res) {
                swal("出错了!", '', 'error');
            },
            success: function(data) {
                if (data.result) {
                    fn(data)
                } else {
                    swal("出错了!", data.error, 'error');
                }
            }
        })
    }
    // 工具函数  获取json
$.jajax = function(url, fn) {
    $.ajax({
        url: url,
        type: 'get',
        dataType: 'json',
        error: function(res) {
            swal("出错了!", '', 'error');
        },
        success: function(data) {
            if (data.result) {
                fn(data)
            } else {
                swal("出错了!", data.error, 'error');
            }
        }
    })
}



// 使用规范
// {
//     name:名字
//     titile:中文
// modal_detail:是否用模态窗展示详情（有隐藏字段没展示）
//     具体字段数据
//     data：[
//         {
//             name:
//             title:
//             type:类型，默认input text
//             select_type：获取数据的action_type的值
//             option_val list的显示字段 默认id
//             option_name list的显示字段 默认name
//             toname:preload数据里，完成id到name得转换显示，select默认true
//             value：select直接从value里渲染，不发ajax和preload，如果没有type，就是input里的value属性
//              hide:默认false，true的话隐藏此字段


//         }
//     ]
// }
var RebootPage = function(opt) {
    var that = this
    // name，决定操作的type
    this.name = opt.name
        // 中文名，显示文字
    this.title = opt.title
        // 初始化data
    this.data = opt.data
    // 垂直滚动 设置高度限制
    this.scrollY = opt.scrollY
    // 是否水平滚动，datatable的设置
    this.scrollX = opt.scrollX
        // 添加地址，addurl或者默认addapi
    this.addurl = opt.addurl || ''
        // 更新地址 默认updateapi
    this.updateurl = opt.updateurl || ''
        // 表单验证数据
    this.validators = {}
    // 是否显示详情按钮
    this.modal_detail = opt.modal_detail
    // 预加载数据，预加载完毕之后，才渲染页面
    this.preload = {}

    //是否有查看子菜单的按钮，比如产品下，点击查看此产品下的业务线
    this.showsub = opt.showsub
    //获取子菜单的key，最终会放在url上，获取list的时候会用这个变量，默认是id
    this.subkey = opt.subkey || 'id'
    //查看子菜单按钮上的文字
    this.subtext = opt.subtext ||'子菜单'
    // 取表中的字段
    this.subname = opt.subname ||'name'
    //url上额外参数 list的时候额外参数
    this.extraParams = {}

    this.hasSub = {}
    $.each(this.data,function(i,v){
        if (v.subselect) {
            that.hasSub[v.name] = v.subselect
        };
    })

    //弹出窗的标签
    this.modalArr = ['<div class="modal fade">',
            '<div class="modal-dialog">',
            '<div class="modal-content">',
            '<div class="modal-header">',
            '<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>',
            '<h4 class="modal-title"></h4>',
            '</div>',
            '<div class="modal-body">',
            '</div>',
            '</div>',
            '</div>',
            '</div>'
        ],
    this.isInit = true

}

var oLanguage = {
    "oAria": {
        "sSortAscending": ": 升序排列",
        "sSortDescending": ": 降序排列"
    },
    "oPaginate": {
        "sFirst": "首页",
        "sLast": "末页",
        "sNext": "下页",
        "sPrevious": "上页"
    },
    "sEmptyTable": "没有相关记录",
    "sInfo": "第 _START_ 到 _END_ 条记录，共 _TOTAL_ 条",
    "sInfoEmpty": "第 0 到 0 条记录，共 0 条",
    "sInfoFiltered": "(从 _MAX_ 条记录中检索)",
    "sInfoPostFix": "",
    "sDecimal": "",
    "sThousands": ",",
    "sLengthMenu": "每页显示条数: _MENU_",
    "sLoadingRecords": "正在载入...",
    "sProcessing": "正在载入...",
    "sSearch": "搜索:",
    "sSearchPlaceholder": "",
    "sUrl": "",
    "sZeroRecords": "没有相关记录"
}
$.fn.dataTable.defaults.oLanguage = oLanguage;
$.extend(RebootPage.prototype, {
    // 启动函数
    init: function() {
        var that = this
        //所有ajax请求
        var arr = []
        // 所有类型
        var typearr = []
        var tmp = {}
        // 有select_type字段的，都是需要预加载的
        $.each(this.data, function(i, v) {
            if (v.select_type) {
                if (tmp[v.select_type]) {

                }else{
                    tmp[v.select_type] = true
                    // if (true) {};
                    var url = '/listapi?action_type=' + v.select_type+that.getUrlParms()
                    // if (v.extra) {
                    //     url += '&'+v.extra
                    // };
                    typearr.push(v)
                        // console.log(url)
                    arr.push($.getJSON(url))

                }
                // console.log(v)
            }else{
                if (v.value) {
                    that.preload[v.name] = v.value
                }
            }

        })
        // 所有ajax请求完成之后，启动页面，预加载的数据存在this.preload中
        $.whenAll.apply($, arr).then(function() {
            // console.log(arguments)
            $.each(arguments, function(index, value) {
                var config = typearr[index]
                var obj 
                if (config.name=='server_purpose') {
                    obj = that.preload['server_purpose'] = {}
                }else{
                    obj = that.preload[config.select_type] = {}
                }
                if (config.name=='service_id') {
                    that.service_top = {}
                    $.each(value[0].result,function(i,v){
                        if (v.pid==0) {
                            that.service_top[v.id] = v.service_name
                        };
                    })
                };
                if (config.value) {

                    $.each(config.value,function(k,v){
                        obj[k] = v
                    })
                };

                // 默认是id=》name，
                var val = config.option_val || 'id'
                var name = config.option_name || 'name'
                if (value[0].result) {                
                    $.each(value[0].result, function(i, v) {
                        obj[v[val]] = v[name]||v.type
                    })
                };

            })
            that.initPage()
        })

    },
    initPage: function() {
        // 启动页面
        var that = this
        that.initForm()
        that.initAddModal()
        that.initUpdateModal()
        if (that.modal_detail) {
            that.initDetailModal()
        };
        that.initAddBtn()
        that.initTable()
        that.getlist()
        that.bindEvents()
        that.getUrl()
            // console.log(that.preload)

    },

    getUrl:function(){
        var that = this
        // extraParams
        $.each(location.search.slice(1).split('&'),function(i,v){
            var tmp = v.split('=')
            that.extraParams[tmp[0]] = tmp[1]
        })
    },
    // 初始化表单 根据传入的opt，循环，拼接bootstrap风格的表单字符串，放倒this上
    // 注意对select和input的不同处理
    initForm: function() {
        var that = this
        var formArr = ['<form class="form-horizontal  ' + this.name + 'Form ">']
        $.each(this.data, function(indev, val) {
            // 表单验证配置
            if (!val.empty) {
                that.validators[val.name] = {
                    validators: {
                        notEmpty: {
                            message: val.msg || '请输入' + val.title
                        }
                    }
                }            
            };

            val.placeholder = val.placeholder || '请输入' + val.title
            val.type = val.type || 'text'
            formArr.push('<div class="form-group">')
            formArr.push('<label class="col-xs-3 control-label">' + val.title + '</label>')
            formArr.push('<div class="col-xs-8">')
            if (val.type == 'select') {
                // console.log(val)
                var optionData = that.preload[val.select_type || val.name]
                // console.log(optionData)
                    // console.log(optionData)
                var temp = ['<select name="' + val.name + '" class="form-control">']
                if (val.name == 'service_id') {
                    $.each(that.service_top, function(k, v) {
                        temp.push('<option value="' + k + '">' + v + '</option>')
                    })

                } else {
                    $.each(optionData, function(k, v) {
                        temp.push('<option value="' + k + '">' + v + '</option>')
                    })
                }
                temp.push('</select>')
                formArr.push(temp.join(''))

            } else if (val.type == 'date') {
                formArr.push('<input type="text" class="form-control input-datepicker" name="' + val.name + '" />')
            } else {
                if (val.value) {
                    formArr.push('<input type="' + val.type + '" value="' + val.value + '" class="form-control" name="' + val.name + '" placeholder="' + val.placeholder + '" />')
                } else {
                    formArr.push('<input type="' + val.type + '"  class="form-control" name="' + val.name + '" placeholder="' + val.placeholder + '" />')
                }

            }
            formArr.push('</div></div>')
        })
        formArr.push('<div class="form-group">' +
            '<label for="" class="col-xs-3 control-label"></label>' +
            '<div class="col-xs-5">' +
            '<input type="submit" class="btn btn-primary">' +
            ' <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>' +
            '</div>' +
            '</div>')
        formArr.push('</form>')
        this.formStr = formArr.join('')
    },
    // initForm之后，加上添加的属性，就是一个添加的表单
    // 设置id 按钮的文字
    initAddForm: function() {
        var that = this
        var addForm = $(this.formStr).attr('id', 'add' + this.name + 'Form')
            .find('[type="submit"]').val('添加').end()
            //添加地址，addurl或者默认add+name
            // addForm.attr('action', this.addurl || 'add' + this.name)
        addForm.attr('action', this.addurl || '/addapi')
        addForm.append('<input type="hidden" name="action_type" value="' + that.name + '">')
        this.addForm = addForm
        this.addFormValidate()
    },
    // initForm之后，加上更新的属性，就是一个更新的表单
    // 设置id 按钮的文字

    initUpdateForm: function() {
        var that = this
        var updateForm = $(this.formStr).attr('id', 'update' + this.name + 'Form')
            .find('[type="submit"]').val('编辑').end()
            // updateForm.attr('action', this.updateurl || 'update' + this.name)
        updateForm.attr('action', this.updateurl || '/updateapi')
        updateForm.append('<input type="hidden" name="action_type" value="' + that.name + '">')
        this.updateForm = updateForm
        this.updateFormValidate()
    },
    // 初始化新增项目的弹出窗，把表单塞进去，最后放到文档里
    initAddModal: function() {
        this.initAddForm()
        this.addModal = $(this.modalArr.join('')).attr('id', 'add' + this.name + 'modal')
            .find('.modal-title').html('添加' + this.title)
            .end()
            .find('.modal-body').append(this.addForm)
            .end()
        $('body').append(this.addModal)
    },
    // 初始化更新项目的modal，只是把表单塞进去，还没有数据渲染
    initUpdateModal: function() {
        this.initUpdateForm()
        this.updateModal = $(this.modalArr.join('')).attr('id', 'update' + this.name + 'modal')
            .find('.modal-title').html('更新' + this.title)
            .end()
            .find('.modal-body').append(this.updateForm)
            .end()
        $('body').append(this.updateModal)
    },
    // 详情弹出窗口
    initDetailModal:function(){
        this.detailModal = $(this.modalArr.join('')).attr('id', 'detail' + this.name + 'modal')
            .find('.modal-title').html( this.title+'详情')
            .end()
        $('body').append(this.detailModal)    
    },
    // 添加一个addBTN在表格上面，和添加的表单对应，点击能打开
    initAddBtn: function() {
        $('#main-content').prepend('<p class="add-btn"><button type="button" class="btn btn-primary btn-sm"' +
            'data-toggle="modal" data-target="#add' + this.name + 'modal">' +
            '添加' + this.title + '</button></p>')
    },
    // 添加表单验证
    addFormValidate: function() {
        var that = this
        that.addForm.formValidation({
            framework: 'bootstrap',
            icon: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            fields: that.validators
        }).off('success.form.fv').on('success.form.fv', function(e) {
            e.preventDefault();
            var $form = $(e.target), // The form instance
                fv = $(e.target).data('formValidation'); // FormValidation instance
            $.rajax($form.attr('id'), function(data) {
                swal("添加成功!", '', 'success');
                that.addForm[0].reset()
                that.addModal.modal('hide')
                that.getlist()
                    // getManu()
            })

        });

    },
    // 更新表单验证
    updateFormValidate: function() {
        var that = this
        that.updateForm.formValidation({
            framework: 'bootstrap',
            icon: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            fields: that.validators
        }).off('success.form.fv').on('success.form.fv', function(e) {
            e.preventDefault();
            var $form = $(e.target), // The form instance
                fv = $(e.target).data('formValidation'); // FormValidation instance
            $.rajax($form.attr('id'), function(data) {
                swal("更新成功!", '', 'success');
                that.updateModal.modal('hide')
                that.updateForm.find('[type="hidden"]').remove()
                    .end().append('<input type="hidden" name="action_type" value="'+that.name+'">')[0].reset()
                that.getlist()
            })

        });
    },
    // 绑定事件，现在之后更新按钮的事件，后续再扩展吧
    bindEvents: function() {
        var that = this
        $('.input-datepicker').datepicker({
            format: "yyyy-mm-dd",
            language: "zh-CN"
        });
        // that.initSelect()
        $(document).off('click.update').on('click.update', '.update', function() {
            var obj = $(this).data()
            $.each(obj, function(key, val) {
                
                if (that.updateForm.find('[name="' + key + '"]').length) {

                    if (that.hasSub[key]) {
                        that.updateForm.find('[name="' + key + '"]').val(val).attr('data-subval',obj[that.hasSub[key]]).trigger('change')

                    }else{
                        that.updateForm.find('[name="' + key + '"]').val(val)

                    }
                } else {
                    that.updateForm.prepend('<input type="hidden" name="' + key + '" value="' + val + '" >')
                }
            })

            that.updateModal.modal('show')
        })
        $(document).off('click.detail').on('click.detail', '.detail', function() {
            var obj = $(this).data()
            var tableArr = ['<table class="table table-bordered table-condensed">']
            $.each(that.data,function(index,value){
                        var name
                        if (value.type == 'select' && value.name !== 'service_id') {
                            var type = value.select_type || value.name
                            name = that.preload[type][obj[value.name]]
                        } else {
                            name = obj[value.name]
                        }

                    tableArr.push('<tr><td>'+value.title+'</td><td>'+name+'</td></tr>')
            })
            tableArr.push('</table>')
            that.detailModal.find('.modal-body').html(tableArr.join(''))
                .end().modal('show')
        })
        $.each(that.data,function(key,val){
            if (val.subselect) {
                var sub = val.subselect
                var key = val.subkey
                var type = val.subtype
                $(document).on('change.sub','[name="'+val.name+'"]',function(){
                    var $this = $(this)
                    var value = $this.val()

                    var dom = $(this)
                    $.jajax('/listapi?action_type='+type+'&'+key+'='+value,function(data){
                        var res = data.result
                        if (res) {
                            var tmp = []
                            $.each(res,function(i,v){
                                tmp.push('<option value="'+v[val.sub_optionkey]+'" >'+v[val.sub_optionname]+'</option>')
                            })
                            var $sub = dom.closest('form').find('[name="'+sub+'"]')
                            $sub.html(tmp.join(''))
                            if ($this.attr('data-subval')) {
                                $sub.val($this.attr('data-subval'))
                            };

                        };
                    })
                })
                $('[name="'+val.name+'"]').trigger('change')
            };
        })
    },
    // 初始化table字符串，表头信息
    initTable: function() {
        var that = this
        var tableArr = ['<table class="table table-bordered">']

        var thead = ['<thead>', '<tr>']
        $.each(that.data, function(i, v) {
            if (!v.hide) {
                thead.push('<th>' + v.title + '</th>')
            };

        })
        thead.push('<th>操作</th></tr></thead>')
        tableArr.push(thead.join(''))
        tableArr.push('<tbody></tbody></table>')
        var table = $(tableArr.join(''))
        this.tbody = table.find('tbody')
        $('#main-content').append(table)
    },
    // 调用ajax接口，获取对应list，listapi，渲染表格
    getlist: function() {
        var that = this
        $.jajax('/listapi?action_type=' + that.name+that.getUrlParms(), function(data) {
            var arr = []
            // 循环result，每个数据是一行
            $.each(data.result, function(i, v) {
                var btn = ['<button class="btn btn-xs btn-primary" ']
                arr.push('<tr>')
                //将数据放在data里,编辑的时候从这里取数据渲染表单
                $.each(v, function(key, val) {
                    if (val || val === 0) {
                        btn.push(' data-' + key + '=' + val)
                    };

                })
                btn.push('></button>')

                // 编辑传进来的data，取每一列的key，再从result的数据里取数据渲染
                // 如果data里hide是true，则隐藏
                $.each(that.data, function(index, value) {
                    // console.log(value)
                    if (!value.hide) {
                        var name
                        // && value.name !== 'service_id'
                        if (value.type == 'select' ) {
                            var type = value.select_type || value.name
                            if (value.name=='server_purpose') {
                                // console.log(value)
                                // console.log(that.preload)
                            };
                            name = that.preload[type][v[value.name]]||unescape(that.extraParams['name'])
                            // alert(1)
                        } else {
                            name = v[value.name]
                        }
                        arr.push('<td>' + name + '</td>')
                    };

                })
                var operateBtn = $(btn.join('')).addClass('update').html('更新').prop('outerHTML')
                if (that.modal_detail) {
                    operateBtn += $(btn.join('')).addClass('detail').html('详细').prop('outerHTML')
                };
                if (that.showsub) {
                    operateBtn += '<a style="margin-left:10px" class="btn btn-xs btn-primary" href="?name='+escape(v[that.subname])+'&'+that.subkey+'='+v[that.subkey]+'">查看'+that.subtext+'</a>'
                };
                arr.push('<td>' + operateBtn+ '</td>')
                arr.push('</td>')

            })
            that.renderDatatable(arr.join(''))

        })
    },

    // 用datatable启动分页和查询，ajax更新的时候，销毁再重新启动
    renderDatatable: function(str) {

        if (!$.fn.dataTable.isDataTable( '.table' )) {
            this.tbody.html(str)
        } else {
            this.datatable.destroy()
            // $('.table').dataTable().fnClearTable(); //清空一下table
            // $('.table').dataTable().fnDestroy(); //还原初始化了的datatable
            this.tbody.html(str)
        }
        // $('.table').DataTable().destory(); 
        var obj = {
            responsive: true,
            bLengthChange: false,            
        } 
        if (this.scrollY) {
            obj.scrollY=this.scrollY
        }
        if (this.scrollX) {
            obj.scrollX=true
        };
        this.datatable = $('.table').DataTable(obj);
    },
    getUrlParms:function(){
        // var that = this
        // extraParams
        var param = location.search.slice(1)
        if (param) {
            return '&'+param
        }else{
            return ''
        }
    }
})
$.rebootOps = function(opt) {
    var reboot = new RebootPage(opt)
    reboot.init()
}


$(function() {

    $('#side-menu').metisMenu();


    $(window).bind("load resize", function() {
        topOffset = 50;
        width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 768) {
            $('div.navbar-collapse').addClass('collapse');
            topOffset = 100; // 2-row-menu
        } else {
            $('div.navbar-collapse').removeClass('collapse');
        }

        height = ((this.window.innerHeight > 0) ? this.window.innerHeight : this.screen.height) - 1;
        height = height - topOffset;
        if (height < 1) height = 1;
        if (height > topOffset) {
            $("#page-wrapper").css("min-height", (height) + "px");
        }
    });

    var url = window.location;
    var element = $('ul.nav a').filter(function() {
        return this.href == url || url.href.indexOf(this.href) == 0;
    }).addClass('active').parent().parent().addClass('in').parent();
    if (element.is('li')) {
        element.addClass('active');
    }
    $('.form-control-static .fa').addClass('text-primary')

});