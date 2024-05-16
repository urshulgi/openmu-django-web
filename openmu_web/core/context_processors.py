from core.website_config import WebsiteConfig


def constant_template_variables(request):
    return {
        "PROJECT_NAME": WebsiteConfig.PROJECT_NAME,
        "MENU": WebsiteConfig.MENU,
    }
