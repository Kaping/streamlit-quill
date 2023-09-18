# streamlit-quill-no-handler

This repo forked from https://github.com/okld/streamlit-quill repository.

The same Quill component, except do not have on-change handlers.
**Therefore, you won't be able to get the return value.**


### Download

```pip install -i https://test.pypi.org/simple/ streamlit-quill-no-handler==0.0.3```

### Code
```
st_quill(
    value="",
    placeholder="",
    html=False,
    toolbar=None,
    history=None,
    preserve_whitespace=True,
    readonly=False,
    key=None
)
```
