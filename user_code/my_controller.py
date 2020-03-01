@Controller('/hello')
class MySimpleController:
    @Get('/')
    def greet_world() -> HttpResponse:
        body = 'hello world'
        return _ok_response(body) 

    @Get('/{name}')
    def greet_name(name: str) -> HttpResponse:
        body = 'hello {}'.format(name)
        return _ok_response(body) 

    def _ok_response(body: str) -> HttpResponse:
        return HttpResponse()  \
            .status(Status.Ok) \
            .with_body(body)
