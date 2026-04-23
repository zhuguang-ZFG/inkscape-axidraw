import logging
from pathlib import Path
from types import SimpleNamespace

from dynamicnestinternal.plot_utils_import import from_dependency_import

dynamicnest_control = from_dependency_import('dynamicnestinternal.axidraw_control')
exit_status = from_dependency_import('ink_extensions_utils.exit_status')
message = from_dependency_import('ink_extensions_utils.message')

root_logger = logging.getLogger()
root_logger.setLevel(logging.ERROR)
root_logger.addHandler(message.UserMessageHandler())

if __name__ == '__main__':
    conf = None
    config_path = Path(__file__).with_name('dynamicnest_conf.py')
    try:
        conf_dict = {}
        exec(config_path.read_text(encoding='utf-8'), {}, conf_dict)
        conf = SimpleNamespace(**conf_dict)
        effect = dynamicnest_control.AxiDrawWrapperClass(params=conf, default_logging=False)
    except (FileNotFoundError, ImportError):
        effect = dynamicnest_control.AxiDrawWrapperClass()
    exit_status.run(effect.affect)
