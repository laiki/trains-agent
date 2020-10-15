from ...backend_config import EnvEntry


ENV_HOST = EnvEntry("TRAINS_API_HOST", "TRAINS_API_HOST")
ENV_WEB_HOST = EnvEntry("TRAINS_WEB_HOST", "TRAINS_WEB_HOST")
ENV_FILES_HOST = EnvEntry("TRAINS_FILES_HOST", "TRAINS_FILES_HOST")
ENV_ACCESS_KEY = EnvEntry("TRAINS_API_ACCESS_KEY", "TRAINS_API_ACCESS_KEY")
ENV_SECRET_KEY = EnvEntry("TRAINS_API_SECRET_KEY", "TRAINS_API_SECRET_KEY")
ENV_VERBOSE = EnvEntry("TRAINS_API_VERBOSE", "TRAINS_API_VERBOSE", type=bool, default=False)
ENV_HOST_VERIFY_CERT = EnvEntry("TRAINS_API_HOST_VERIFY_CERT", "TRAINS_API_HOST_VERIFY_CERT", type=bool, default=True)
ENV_CONDA_ENV_PACKAGE = EnvEntry("TRAINS_CONDA_ENV_PACKAGE", "TRAINS_CONDA_ENV_PACKAGE")
