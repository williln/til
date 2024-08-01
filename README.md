# til

My repo of Today I Learned posts. Inspired by [simonw/til](https://github.com/simonw/til). 

**Now**: July 2024: At some point this month, I set a goal to write a TIL every work day. I haven't stuck to that, but I am averaging several per week, and I'm pleased with the cadence. But even trying to post every day, I am still not capturing everything I've learned. 

## My TIL Philosophy 

Since this repo has a few stars ⭐ (hi everyone), I want to take a moment to set expectations. 

- I write TILs quickly, usually in under 10 minutes.
- Usually, there isn't any editing other than light proofreading.
- I really enjoy it! Highly recommend a public TIL repo as a personal practice.
- Sometimes I share them on Mastodon, but not always.

## Benefits of my TIL repo 

- It's good, low-stakes writing practice. 
- It helps remind me that beginnerhood is perpetual. 
- I have a few of my own TILs that I consult really regularly. Nothing beats copying and pasting your own stuff forever. 
- Sometimes, the TILs get picked up by [Django News](https://django-news.com/issues/243?#start), and that's neat! 
- Other people are aware of what I am working on, and then ask for help related to those things. Feels great to help people.
- It provides a neat fossil record of the kinds of things I've worked on over the course of my career.
- I have a repo full of markdown that's easy to clone and run parsing experiments on. 

---

## Topics

<!-- toc starts -->
* [aws](#aws)
* [celery](#celery)
* [django](#django)
* [django-rest-framework](#django-rest-framework)
* [drf-yasg](#drf-yasg)
* [fast-ai](#fast-ai)
* [git](#git)
* [github](#github)
* [google](#google)
* [home-office](#home-office)
* [html](#html)
* [htmx](#htmx)
* [javascript](#javascript)
* [kubernetes](#kubernetes)
* [mac](#mac)
* [markdown](#markdown)
* [meilisearch](#meilisearch)
* [microsoft-dynamics](#microsoft-dynamics)
* [misc](#misc)
* [mkdocs](#mkdocs)
* [postgres](#postgres)
* [pre-commit](#pre-commit)
* [pytest](#pytest)
* [python](#python)
* [r](#r)
* [slack](#slack)
* [sphinx](#sphinx)
* [stripe](#stripe)
* [terraform](#terraform)
* [wagtail](#wagtail)
<!-- toc ends -->

---

<!-- index starts -->
### aws

* [AWS S3 and Boto3 Cheat Sheet](https://github.com/williln/til/blob/main/aws/s3_and_boto_and_minio.md) - 2024-03-18

### celery

* [Scheduling a nightly Celery task with Celery Beat](https://github.com/williln/til/blob/main/celery/schedule_nightly_task.md) - 2024-05-08

### django

* [Adding a custom context processor to your Django app so you can include bits of data in your template headers more easily](https://github.com/williln/til/blob/main/django/add_context_processor.md) - 2024-05-29
* [Adding a custom field to the Django admin list display](https://github.com/williln/til/blob/main/django/custom_fields.md) - 2024-03-18
* [Adding a custom tag with `django-taggit`](https://github.com/williln/til/blob/main/django/django-taggit-custom-tag.md) - 2022-11-09
* [Adding ability to search in the Django Admin](https://github.com/williln/til/blob/main/django/add_search.md) - 2024-03-18
* [Adding extra fields to the list view in the Django Admin](https://github.com/williln/til/blob/main/django/add_fields_to_list_view.md) - 2024-03-18
* [Adding filtering functionality to the Django Admin](https://github.com/williln/til/blob/main/django/add_filtering.md) - 2024-03-18
* [Caching in Django Projects](https://github.com/williln/til/blob/main/django/caching.md) - 2023-04-19
* [Finding out how many objects have N connections to the other model in a M2M relationship](https://github.com/williln/til/blob/main/django/m2m_queries_how_many_objects_have_no_connections.md) - 2024-02-28
* [Finding the longest value of a particular field](https://github.com/williln/til/blob/main/django/longest_value_in_field.md) - 2024-02-28
* [Handling 404 Responses in Django](https://github.com/williln/til/blob/main/django/404_handling.md) - 2023-04-19
* [How I added a very simple django-streamfield example to a project](https://github.com/williln/til/blob/main/django/how_I_added_django_streamfield.md) - 2024-03-18
* [How I set up `django-activity-stream`, including a simple test](https://github.com/williln/til/blob/main/django/how_i_added_django_activity_stream_with_test.md) - 2024-03-25
* [How to confirm that login is required in your Django view](https://github.com/williln/til/blob/main/django/how_to_test_view_auth.md) - 2023-02-22
* [How to log in a test user in a `pytest` unit test](https://github.com/williln/til/blob/main/django/test_protected_page.md) - 2023-02-22
* [How to test a file upload with `pytest` and `SimpleUploadedFile`](https://github.com/williln/til/blob/main/django/testing_file_upload_pytest.md) - 2023-02-22
* [Neapolitan: Everything I've Learned](https://github.com/williln/til/blob/main/django/neapolitan.md) - 2024-08-01
* [Run SQL statements as part of your migrations with `migrations.RunSQL`](https://github.com/williln/til/blob/main/django/run_sql.md) - 2024-07-23
* [Testing Django signals, and disabling signals in tests (Django 2.2)](https://github.com/williln/til/blob/main/django/testing_django_signals.md) - 2020-07-27
* [Using `Coalesce` to provide a default value for `aggregate` queries](https://github.com/williln/til/blob/main/django/aggregation_coalesce.md) - 2021-02-18
* [Using `defer()` to limit the data you get from your models](https://github.com/williln/til/blob/main/django/defer.md) - 2022-10-19
* [Using `django-admin-env-notice` to add an envioronment notice to the frontend](https://github.com/williln/til/blob/main/django/add_env_banner_to_frontend.md) - 2024-06-20
* [Using `django-countries`](https://github.com/williln/til/blob/main/django/django_countries.md) - 2024-04-02
* [Using `iterator()` to loop through large querysets efficiently](https://github.com/williln/til/blob/main/django/iterator.md) - 2024-07-10
* [Using Django Aggregation](https://github.com/williln/til/blob/main/django/aggregation.md) - 2021-01-22
* [Using Enums in a Django Model ChoiceField (Django 2.2)](https://github.com/williln/til/blob/main/django/enums_as_choices.md) - 2020-05-26
* [Using inline formsets with `inlineformset_factory`](https://github.com/williln/til/blob/main/django/using_inline_formsets.md) - 2024-06-03
* [Why won't my Django file URLs come back signed from S3?](https://github.com/williln/til/blob/main/django/aws_signed_urls.md) - 2021-01-08

### django-rest-framework

* [Adding a custom pagination class to an action](https://github.com/williln/til/blob/main/django-rest-framework/custom_action_pagination.md) - 2022-10-25
* [Passing extra info in `context` to your DRF serializer](https://github.com/williln/til/blob/main/django-rest-framework/pass_to_context.md) - 2021-01-22

### drf-yasg

* [How to document your query parameters for `drf_yasg`](https://github.com/williln/til/blob/main/drf-yasg/query_params.md) - 2021-01-28
* [How to properly serialize a `serializer_method_field` with `drf_yasg`](https://github.com/williln/til/blob/main/drf-yasg/serializer_method_field.md) - 2021-01-28
* [How to serialize your request parameters for POST/PUT/PATCH requests](https://github.com/williln/til/blob/main/drf-yasg/define_request_body.md) - 2021-01-28

### fast-ai

* [Converting a `fastcore.basics.AttrDict` into a regular dictionary.](https://github.com/williln/til/blob/main/fast-ai/obj2dict.md) - 2024-03-18

### git

* [`git reset`, with `soft`: Undo your last commit but keep your changes](https://github.com/williln/til/blob/main/git/undo_commit_but_preserve_changes.md) - 2024-07-29
* [Moving from an old repo to a new repo in another organization](https://github.com/williln/til/blob/main/git/moving_to_a_new_repo.md) - 2024-05-13

### github

* [Commenting on an issue from a GitHub Action](https://github.com/williln/til/blob/main/github/gh-actions-comment-issue.md) - 2022-11-04
* [Creating a new file and committing it using a GitHub Action](https://github.com/williln/til/blob/main/github/gh-actions-step-to-create-and-commt-a-file.md) - 2022-11-04
* [Github Action that leaves a comment on new PRs or issues](https://github.com/williln/til/blob/main/github/action_pr_comment.md) - 2022-10-28
* [How to use a Github Action](https://github.com/williln/til/blob/main/github/howto_github_action.md) - 2020-05-26
* [Making one job in a workflow depend on another job](https://github.com/williln/til/blob/main/github/gh-actions-set-job-dependency.md) - 2022-11-04
* [Parsing JSON output from a GitHub Issue template in a GitHub Action](https://github.com/williln/til/blob/main/github/gh-actions-parse-json.md) - 2022-11-04
* [Running an action conditionally](https://github.com/williln/til/blob/main/github/gh-action-run-job-conditionally.md) - 2022-11-04
* [Running your tests with `pytest` in your PR via a GitHub Action](https://github.com/williln/til/blob/main/github/gh-action-test-ci.md) - 2024-07-24
* [Setting output for a step in a job, so a different job can use it](https://github.com/williln/til/blob/main/github/gh-action-set-output.md) - 2022-11-04
* [Temporarily disabling a GitHub action without touching the workflow file](https://github.com/williln/til/blob/main/github/gh_actions_temporary_disable.md) - 2022-11-07

### google

* [Using Google Cloud Service Accounts and authenticating as a dictionary (without the json file) in a Django project](https://github.com/williln/til/blob/main/google/using_service_account_as_dict.md) - 2024-03-01

### home-office

* [Troubleshooting my Brother HL-2270DW Wireless Printer](https://github.com/williln/til/blob/main/home-office/printer.md) - 2024-03-18

### html

* [Creating responsive images with `srcset`, `sizes`, and `<picture>`](https://github.com/williln/til/blob/main/html/responsive_images_with_picture_element.md) - 2024-06-05
* [Stop search engines from indexing your site and showing it in search results](https://github.com/williln/til/blob/main/html/stop_google_from_indexing_your_site.md) - 2024-06-12

### htmx

* [Making a simple `hx-get` request](https://github.com/williln/til/blob/main/htmx/making_an_hxget_request.md) - 2024-05-16
* [Updating other elements on the page with `hx-swap-oob`](https://github.com/williln/til/blob/main/htmx/out_of_band_swaps.md) - 2024-06-03

### javascript

* [TimelineJS for building interactive timelines from spreadsheet or JSON](https://github.com/williln/til/blob/main/javascript/timelinejs.md) - 2024-05-22

### kubernetes

* [Accessing a Kubernetes cluster for the first time](https://github.com/williln/til/blob/main/kubernetes/accessing_cluster.md) - 2024-05-14
* [Setting up Kubernetes access on MacOS with a config file](https://github.com/williln/til/blob/main/kubernetes/setting_up_new_access_mac.md) - 2024-05-14
* [Viewing logs for your pod](https://github.com/williln/til/blob/main/kubernetes/viewing_logs.md) - 2024-07-30

### mac

* [Control when your laptop locks, turns off the display, etc.](https://github.com/williln/til/blob/main/mac/control_when_machine_locks.md) - 2024-05-22

### markdown

* [Making a collapsible markdown section](https://github.com/williln/til/blob/main/markdown/collapsible_markdown.md) - 2022-11-05

### meilisearch

* [Securing Meilisearch with Docker for local Django development](https://github.com/williln/til/blob/main/meilisearch/securing_meilisearch_in_docker.md) - 2024-04-04
* [Securing the Meilisearch search itself](https://github.com/williln/til/blob/main/meilisearch/securing_meilisearch_search.md) - 2024-04-05
* [Setting up Meilisearch with Python, Docker, and Compose for local development](https://github.com/williln/til/blob/main/meilisearch/setting_up_meilisearch_python_docker.md) - 2024-04-04

### microsoft-dynamics

* [About Microsoft Dynamics](https://github.com/williln/til/blob/main/microsoft-dynamics/about-microsoft-dynamics.md) - 2024-05-29

### misc

* [Relume Design League - competitive web design](https://github.com/williln/til/blob/main/misc/competitive_web_design.md) - 2022-11-05

### mkdocs

* [Including your project's README on your MkDocs index page](https://github.com/williln/til/blob/main/mkdocs/include_readme_in_index.md) - 2024-07-08

### postgres

* [Collecting statistics about your database with `ANALYZE`](https://github.com/williln/til/blob/main/postgres/analyze.md) - 2024-07-23

### pre-commit

* [Setting up `pre-commit` in a new project](https://github.com/williln/til/blob/main/pre-commit/setup.md) - 2024-06-28

### pytest

* [Test that an exception is raised](https://github.com/williln/til/blob/main/pytest/assert_raises.md) - 2023-03-02

### python

* [ChatGPT-4 distills the Python `mailbox` docs for me.](https://github.com/williln/til/blob/main/python/mailbox.md) - 2023-04-24
* [Create a new Python virtual environment](https://github.com/williln/til/blob/main/python/new-virtualenv.md) - 2022-10-14
* [Generate a markdown file with a table of contents in Python](https://github.com/williln/til/blob/main/python/generate-toc.md) - 2022-10-28
* [Generating a clickable table-of-contents for each directory in my TILs](https://github.com/williln/til/blob/main/python/generate_toc_for_subdirectory.md) - 2024-06-03
* [How to sort a Python dictionary by key or value](https://github.com/williln/til/blob/main/python/sort_dictionary.md) - 2021-02-02
* [How to sort a Python dictionary by multiple values](https://github.com/williln/til/blob/main/python/sort_dict_multiple_keys.md) - 2021-02-02
* [Using `Decimal.quantize`](https://github.com/williln/til/blob/main/python/decimal_quantize.md) - 2024-07-05
* [Using `pip-tools` and `pip-compile` for Python dependency management](https://github.com/williln/til/blob/main/python/pip_tools.md) - 2024-07-17

### r

* [`taylor`: The Taylor Swift / R Project](https://github.com/williln/til/blob/main/r/taylor_swift.md) - 2023-04-21
* [How to convert an `.rda` file to JSON](https://github.com/williln/til/blob/main/r/convert_rda_to_json.md) - 2023-04-21

### slack

* [Keep Slack from kicking you out of huddles when your machine locks](https://github.com/williln/til/blob/main/slack/computer_locking_kicks_out_of_huddles.md) - 2024-05-22

### sphinx

* [Running Sphinx docs locally](https://github.com/williln/til/blob/main/sphinx/running_locally.md) - 2024-07-15

### stripe

* [`dj-stripe` contains models for all the Stripe objects and can sync them for you](https://github.com/williln/til/blob/main/stripe/setup-dj-stripe.md) - 2024-07-18
* [Creating a PaymentIntent, but not capturing it, and allowing more to be charged later](https://github.com/williln/til/blob/main/stripe/uncaptured_payment_intents_and_overcapture.md) - 2024-06-10
* [Generating a `PaymentIntent` and saving it to a Django model](https://github.com/williln/til/blob/main/stripe/payment_intents.md) - 2024-06-06
* [Receiving Stripe webhooks via `dj-stripe` in local dev](https://github.com/williln/til/blob/main/stripe/using_dj_stripe_webhooks_locally.md) - 2024-07-19
* [Setting up a webhook in local development (Django project)](https://github.com/williln/til/blob/main/stripe/webhook_local_dev.md) - 2024-07-11
* [Using off-session payments and `setup_future_usage`](https://github.com/williln/til/blob/main/stripe/off_session_payments.md) - 2024-06-06

### terraform

* [About Terraform and .tfvars files](https://github.com/williln/til/blob/main/terraform/tfvars-files.md) - 2024-07-15

### wagtail

* [Add Wagtail to an existing Django project](https://github.com/williln/til/blob/main/wagtail/add_to_existing_project.md) - 2024-02-26
* [Adding a Wagtail image programmatically](https://github.com/williln/til/blob/main/wagtail/add_image_programmatically.md) - 2024-07-01
* [Cheat Sheet for Wagtail StreamField](https://github.com/williln/til/blob/main/wagtail/cheat_sheet_wagtail_streamfield.md) - 2024-02-26
* [Cheat Sheet: Wagtail Page Model Fields](https://github.com/williln/til/blob/main/wagtail/cheat_sheet_wagtail_page_model_fields.md) - 2024-02-26
* [Choosing Between Wagtail Page Models and Django Models](https://github.com/williln/til/blob/main/wagtail/choosing_wagtail_page_models_vs_django_models.md) - 2024-02-26
* [Create a Custom Nested Block for Wagtail StreamField](https://github.com/williln/til/blob/main/wagtail/create_custom_nested_block_for_streamfield.md) - 2024-02-26
* [Creating Custom StreamField Blocks](https://github.com/williln/til/blob/main/wagtail/create_custom_streamfield_block.md) - 2024-02-26
* [Creating Wagtail pages with Streamfield content programmatically](https://github.com/williln/til/blob/main/wagtail/creating_streamfield_content_programmatically.md) - 2024-05-15
* [Example of linking Django models to Wagtail Page models](https://github.com/williln/til/blob/main/wagtail/example_integrating_wagtail_page_models_into_django_models.md) - 2024-02-26
* [Seeding my Wagtail site](https://github.com/williln/til/blob/main/wagtail/seeding_wagtail_site.md) - 2024-03-27
* [What to do if you delete the default Wagtail homepage](https://github.com/williln/til/blob/main/wagtail/fix_deleted_root_page.md) - 2024-03-25
<!-- index ends -->
