import json

from django.utils import translation
from wagtailtinymce.rich_text import TinyMCERichTextArea
from django.conf import settings

from wagtail.admin.rich_text.converters.editor_html import WhitelistRule
from wagtail.core import hooks
from wagtail.core.whitelist import allow_without_attributes

from django.templatetags.static import static
from django.utils import translation
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from wagtail.core import hooks
from wagtailtinymce.wagtail_hooks import to_js_primitive

from wagtail.core.whitelist import attribute_rule, check_url, allow_without_attributes

class TinyMCEWrapper(TinyMCERichTextArea):
    def __init__(self, *args, **kwargs):
        translation.trans_real.activate(settings.LANGUAGE_CODE)
        super(TinyMCEWrapper, self).__init__(*args, **kwargs)
        self.kwargs['buttons'][0].append(['codesample code'])
        print("TinyMCE: Successfully Initialized")

    def render_js_init(self, id_, name, value):
        """Overriden from base class to get complete control over editor init"""
        kwargs = {
            'options': self.kwargs.get('options', {}),
        }

        if 'buttons' in self.kwargs:
            if self.kwargs['buttons'] is False:
                kwargs['toolbar'] = False
            else:
                kwargs['toolbar'] = [
                    ' | '.join([' '.join(groups) for groups in rows])
                    for rows in self.kwargs['buttons']
                ]

        if 'menus' in self.kwargs:
            if self.kwargs['menus'] is False:
                kwargs['menubar'] = False
            else:
                kwargs['menubar'] = ' '.join(self.kwargs['menus'])

        kwargs['codesample_languages'] = [
         {'text': 'HTML/XML', 'value': 'markup'},
         {'text': 'JavaScript', 'value': 'javascript'},
         {'text': 'CSS', 'value': 'css'},
         {'text': 'PHP', 'value': 'php'},
         {'text': 'Ruby', 'value': 'ruby'},
         {'text': 'Python', 'value': 'python'},
         {'text': 'Java', 'value': 'java'},
         {'text': 'C', 'value': 'c'},
         {'text': 'C#', 'value': 'csharp'},
         {'text': 'C++', 'value': 'cpp'}]
        kwargs['extended_valid_elements']='span[class]'

        return "makeTinyMCEEditable({0}, {1});".format(json.dumps(id_), json.dumps(kwargs))


@hooks.register('register_rich_text_features')
def whitelister_element_rules(features):
    # Values taken from wagtail/core/whitelist.py:67
    allow_with_inline_style = attribute_rule({'style': True, 'id': True})

    rules = {
        'a': attribute_rule({'href': check_url, 'style': True}),
        'img': attribute_rule({'src': check_url, 'width': True, 'height': True,
                               'alt': True}),
        '[document]': allow_with_inline_style,
        'b': allow_with_inline_style,
        'br': allow_with_inline_style,
        'div': allow_with_inline_style,
        'em': allow_with_inline_style,
        'h1': allow_with_inline_style,
        'h2': allow_with_inline_style,
        'h3': allow_with_inline_style,
        'h4': allow_with_inline_style,
        'h5': allow_with_inline_style,
        'h6': allow_with_inline_style,
        'hr': allow_with_inline_style,
        'i': allow_with_inline_style,
        'li': allow_with_inline_style,
        'ol': allow_with_inline_style,
        'p': allow_with_inline_style,
        'strong': allow_with_inline_style,
        'sub': allow_with_inline_style,
        'sup': allow_with_inline_style,
        'ul': allow_with_inline_style,

        'table': attribute_rule({'style': True, 'class': True}),
        'thead': allow_with_inline_style,
        'tbody': allow_with_inline_style,
        'th': allow_with_inline_style,
        'td': allow_with_inline_style,
        'tr': allow_with_inline_style,

        'blockquote': allow_with_inline_style,
        'code': allow_with_inline_style,
        'pre': attribute_rule({'style': True, 'class': True, 'contenteditable': False}),
        'span': attribute_rule({'style': True, 'class': True})
    }

    for key, val in rules.items():
        features.register_converter_rule('editorhtml', key, [ WhitelistRule(key, val) ] )
        features.register_converter_rule('contentstate', key, [ WhitelistRule(key, val) ] )

        # add key (e.g. blockquote) to the default feature set
        features.default_features.append(key)
    print("TinyMCE: Completed adding whitelist features")


@hooks.register('insert_tinymce_js')
def tinymce_codesample():
    return format_html(
        """
        <script>
            registerMCEPlugin("codesample", {});
        </script>
        """,
        mark_safe(json.dumps(static('wagtailtinymce/js/vendor/tinymce/plugins/codesample/plugin.min.js'))),
        to_js_primitive(translation.to_locale(translation.get_language())),
    )
