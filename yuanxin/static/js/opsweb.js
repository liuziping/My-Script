function addMasking(options) {
    /*options是一个对象，对象上有一个data属性 绑定事件传进来的数据挂载在data上
    * $('#myModal').on('click',{name:'加载中'},masking)
    * */
    var name;
    var height;
    if(typeof options =='undefined'){
        name = '正在加载中';
    }else{
        name = options;
    }
    $('body').append('<div class="modal fade" id="modal-loading" aria-hidden="true"><div class="content-loading" id="content-loading">'+name+'<span class="ellipsis">.</span><span class="ellipsis2">.</span><span class="ellipsis3">.</span><span class="ellipsis4">.</span><span class="ellipsis5">.</span></div></div>');
    height=$(document).height()-80;
    $('#content-loading').css('lineHeight',height+'px');
    $('#modal-loading').modal('show');
}
function removeMasking() {
    $('.modal-backdrop').remove();
    $('#modal-loading').remove()
}