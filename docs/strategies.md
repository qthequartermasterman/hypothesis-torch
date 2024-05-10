# What you can generate and how

`hypothesis-torch` tries to make most things easy to generate while also allowing the user to customize strategies.

In absense of another justification, `hypothesis-torch` will generally default to generating the widest possible set
of valid objects for a strategy. This means that, for example, `tensor_strategy` (unless configured otherwise) will 
often generate examples with less common layouts (such as sparse tensors) or memory formats (like channels last). For
many use cases, these are too broad, and can be configured to be more specific.

This document is a reference for the strategies that `hypothesis-torch` provides, and how to use them.

## Strategies

::: hypothesis_torch
    handler: python 
    options:
        filters: ["strategy"]
        show_source: false
        group_by_category: true
        allow_inspection: true
        show_root_heading: false
        show_root_toc_entry: false
