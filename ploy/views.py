from pyramid.view import view_config
from ploy.root import Root
from ploy.githubevents import GithubEvents
from ploy.builds import Builds
from ploy.build import createBuild, Build


@view_config(context=Root, renderer='templates/root.mako')
def get_root(request):
    return {}


@view_config(context=GithubEvents, request_method='GET',
             renderer='templates/github_events.mako')
def get_github_events(request):
    return {'events':request.context}


@view_config(context=GithubEvents, request_method='POST',
             renderer='templates/github_events.mako')
def post_github_events(request):
    event = request.headers.get('X-GitHub-Event')
    ts = request.dependencies.getClock().now()
    message = {'event':event, 'payload': request.json_body, 'received':ts}
    request.context.append(message)
    newBuild = createBuild(request.dependencies, message)
    newBuild.__parent__ = request.root.builds
    request.root.builds.append(newBuild)
    request.response.body = 'Received by Ploy.'
    return request.response


@view_config(context=Builds, request_method='GET',
             renderer='templates/builds.mako')
def get_builds(request):
    return {'builds': request.context}

@view_config(context=Build, request_method='GET',
             renderer='templates/build.mako')
def get_build(request):
    return {'build': request.context}