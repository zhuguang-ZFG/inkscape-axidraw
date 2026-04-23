import logging

from dynamicnestinternal.plot_utils_import import from_dependency_import

dynamicnest_reorder = from_dependency_import('dynamicnestinternal.axidraw_svg_reorder')
exit_status = from_dependency_import('ink_extensions_utils.exit_status')
message = from_dependency_import('ink_extensions_utils.message')

root_logger = logging.getLogger()
root_logger.setLevel(logging.ERROR)
root_logger.addHandler(message.UserMessageHandler())

if __name__ == '__main__':
    effect = dynamicnest_reorder.ReorderEffect()
    exit_status.run(effect.affect)
