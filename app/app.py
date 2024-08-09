import json

import streamlit as st
from jinja2 import BaseLoader, Environment


@st.cache_data
def get_jinja_env() -> 'Environment':
    return Environment(loader=BaseLoader())


def main():
    st.title('Jinja2 Templates')
    st.sidebar.markdown('''
    References:
    - [Jinja2 documentation](https://jinja.palletsprojects.com/en/3.1.x/).
    ---
    ''')

    template_file_str = ''
    if template_file := st.sidebar.file_uploader(
            'Import template from file',
            type=['jinja']
    ):
        template_file_str = template_file.getvalue().decode('utf-8')

    data_file_str = '{}'
    if data_file := st.sidebar.file_uploader(
            'Import data from file',
            type=['json']
    ):
        data_file_str = data_file.getvalue().decode('utf-8')

    template_str = st.text_area(
        'Template',
        value=template_file_str,
        help='Must be a valid Jinja Template.'
    )
    st.download_button('Download template', template_str, file_name='template.jinja')

    data_str = st.text_area(
        'Data',
        value=data_file_str,
        help='Must be a valid JSON.'
    ) or '{}'
    st.download_button('Download data', data_str, file_name='data.json')

    if st.button('Render', use_container_width=True) and template_str and data_str:
        st.header('Render')
        template = get_jinja_env().from_string(template_str)
        data = json.loads(data_str)
        template_rendered = template.render(**data)
        st.text(template_rendered)


if __name__ == '__main__':
    st.set_page_config(
        page_title='Jinja2 Templates',
        initial_sidebar_state='expanded',
    )
    main()
