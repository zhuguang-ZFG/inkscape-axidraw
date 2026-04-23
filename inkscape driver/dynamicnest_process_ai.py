import logging

from dynamicnestinternal.plot_utils_import import from_dependency_import

dynamicnest_process_ai = from_dependency_import('dynamicnestinternal.process_ai')
exit_status = from_dependency_import('ink_extensions_utils.exit_status')
message = from_dependency_import('ink_extensions_utils.message')

root_logger = logging.getLogger()
root_logger.setLevel(logging.ERROR)
root_logger.addHandler(message.UserMessageHandler())

if __name__ == '__main__':
    effect = dynamicnest_process_ai.ProcessAI()
    exit_status.run(effect.affect)
