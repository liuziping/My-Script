# _*_ coding: utf-8 _*_
import gitlab

from opsweb.settings import GITLAB_HTTP_URI, GITLAB_TOKEN


gl = gitlab.Gitlab(GITLAB_HTTP_URI, GITLAB_TOKEN)


def get_user_projects(request):
    """
        1: 获取gitlab里所有的项目，
        2: 当前登录用户所拥有的项目
    """
    
    user_projects = []
    all_projects = gl.projects.list()

    # 查出所有项目中包含登录用户的项目
    for project in all_projects:
        for member in project.members.list():
            if member.username == request.user.username:
                user_projects.append(project)

    print "user projects %s" % user_projects


    # 查出用户在devops中的组
    user_groups = request.user.groups.all()
    print "user group is %s" % user_groups
    
    # 查出devops平台组对应gitlab中的组信息，两者同名，但不一定同id
    gitlab_user_groups = []
    for group in user_groups:
        gitlab_user_groups.extend(gl.groups.search(group.name))
    print "gitlab_user_groups is %s" % gitlab_user_groups
    

    # 查出用户所在组包含的项目
    group_projects = []
    for group in gitlab_user_groups:
        group_projects.extend(group.projects.list())
    print "group projects is %s" % group_projects

    # 将个人用户对应的项目和个人所在组对应的项目集合并去重
    for user_project in user_projects:
        for group_project in group_projects:
            if user_project.name == group_project.name:
                user_projects.remove(user_project)

    user_projects.extend(group_projects)

    return all_projects, user_projects



