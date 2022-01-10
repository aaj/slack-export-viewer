import flask
from pathlib import Path


def export_channel(channel_name, messages, path):
    html = flask.render_template(
        'viewer.html',
        messages=messages,
        name=channel_name,
        no_sidebar=True,
        no_external_references=False
    )
    with open(path, 'w') as fo:
        fo.write(html)


def export_public_channels():
    Path('output/public').mkdir(parents=True, exist_ok=True)
    channels = list(flask._app_ctx_stack.channels.keys())
    for channel_name in channels:
        messages = flask._app_ctx_stack.channels[channel_name]
        path = f'output/public/{channel_name}.html'
        export_channel(channel_name, messages, path)


def export_private_channels():
    Path('output/private').mkdir(parents=True, exist_ok=True)
    channels = list(flask._app_ctx_stack.groups.keys())
    for channel_name in channels:
        messages = flask._app_ctx_stack.groups[channel_name]
        path = f'output/private/{channel_name}.html'
        export_channel(channel_name, messages, path)
