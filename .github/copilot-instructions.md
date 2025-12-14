# Django Personal Site - Copilot Instructions

## Project Architecture

This is a Django 5.1 personal blog built with modern Python tooling (uv) and designed for Render deployment. The project follows a simple but effective structure:

- **Core apps**: `blog` (content management), `accounts` (custom user model)
- **Custom user model**: `accounts.CustomUser` extends `AbstractUser` (required for all auth operations)
- **Database**: SQLite for development, PostgreSQL for production via `dj_database_url`
- **Static files**: Handled by WhiteNoise in production, standard Django serving in development

## Key Development Patterns

### Package Management & Environment
- Use `uv` for all Python package management (not pip/pipenv/poetry)
- Dependencies in `pyproject.toml` with dev group for development-only packages
- Run commands with `uv run` prefix: `uv run manage.py runserver`
- Quick dev server: `make dev` (runs `uv run manage.py runserver`)

### Database & Models
- All models use `BigAutoField` as primary key (see `DEFAULT_AUTO_FIELD`)
- Blog posts use markdown content with built-in rendering via `markdown` library
- Custom user model is mandatory - always use `accounts.CustomUser` for user references
- Published/unpublished posts controlled by `Post.published` boolean field

### URL Patterns & Views
- Blog posts follow SEO-friendly pattern: `/blog/<year>/<slug>/`
- Main site routes in `personal_site/urls.py`, blog routes in `blog/urls.py`
- RSS feed available at `/blog/feed/` via `blog.feed.BlogFeed`
- Debug toolbar automatically enabled in development mode

### Templates & Static Files
- Global templates in `templates/` directory (base.html, home.html, about.html)
- Uses MVP.css framework for styling: `https://andybrewer.github.io/mvp/mvp.css`
- Static files collected to `staticfiles/` for production deployment

## Environment Configuration

### Development Setup
```bash
uv sync                    # Install dependencies
uv run manage.py migrate   # Setup database
uv run manage.py runserver # Start dev server
```

### Production Settings
- `DEBUG = "RENDER" not in os.environ` - automatic debug detection
- Database URL via `DATABASE_URL` environment variable
- Static files served by WhiteNoise with compression
- `RENDER_EXTERNAL_HOSTNAME` automatically added to `ALLOWED_HOSTS`

## Deployment (Render)
- Deployment config in `render.yaml` - PostgreSQL database + web service
- Build script: `build.sh` (uv sync, collectstatic, migrate)
- ASGI deployment with Gunicorn + Uvicorn workers
- Free tier configuration included

## Development Tools
- Django Debug Toolbar enabled for `127.0.0.1` in development
- `django-extensions` available for enhanced management commands
- Custom user model prevents auth migration issues

## Critical Conventions
- Always use `uv run` for Django commands
- Blog content is markdown-based, rendered in templates
- Year-based URL slugs for posts (enables chronological organization)
- Development uses SQLite, production uses PostgreSQL seamlessly via DATABASE_URL

## Styling
- Uses MVP.css framework for a clean, minimal design
MVP.css works with the following HTML elements:
```html
    <a> — text links
        <a><b>, <a><strong> — solid link buttons
        <a><em>, <a><i> — outlined link buttons
    <article> — content area with normal styling
        <article><aside> — text callout
    <blockquote> — quote callout
        <blockquote><footer> — quote attribution
    <body> — default parent element
    <button> — form buttons
    <code> — inline code highlighting
    <details> — default expandable content section
        <details><summary> — expandable heading
    <dialog> — popup windows
    <div> — unstyled element
    <figure> — image callouts
        <figure><figcaption> — image callout captions
    <footer> — footer area
    <form> — small form area
        <form><input> — short input field
        <form><label> — form field labels
        <form><select> — dropdown options container
            <form><select><option> — dropdown option items
        <form><textarea> — large input field
    <header> — content area with centered styling
    <h1>, <h2>, <h3>, <h4>, <h5>, <h6> — headings
    <hr> — horizontal rule (divider)
    <main> — main content area
    <mark> — text highlighting
    <nav> — top navigation
        <nav><ul> — nav links container
        <nav><ul><li> — nav link items
        <nav><ul><li><ul> — nav dropdown container
        <nav><ul><li><ul><li> — nav dropdown link items
    <ol> — numbered list container
        <ol><li> — numbered list items
    <p> — paragraph tag
    <pre> — preformatted text
        <pre><code> — code block
        <pre><samp> — computer output block
    <samp> — inline computer output
    <section> — content area for centered / special content
        <section><aside> — content card
    <small> — smaller text
    <sup> — raised text (notification bubbles)
    <table> — data table
        <table><td> — data table cell
        <table><th> — data table header cell
        <table><thead> — data table header section
        <table><tr> — data table row
    <ul> — unordered list container
        <ul><li> — unordered list item
```