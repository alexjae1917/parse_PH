import settings
from parse_work.Request import RequestEngine


def main():
    request_engine  = RequestEngine()
    page = settings.START_PAGE

    while True:
        page = settings.START_PAGE

        response = request_engine.get_response(settings.HOST + settings.ROOT_PATH, {
            'page': page})
        print()
        # if not cards :
        #     break


if __name__ == '__main__':
    main()