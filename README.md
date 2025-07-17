# Flask Expense Tracker

[Python | Flask] Simple expense tracker with dashboard

## Setup

For the development we are using [uv](https://github.com/astral-sh/uv), an extremely fast Python package and project manager, written in Rust.

```bash
uv run main.py
```

For the tailwind css we are using [Tailwind Flask Starter](https://github.com/themesberg/tailwind-flask-starter). In order to use it, if not installed yet, run:

```bash
npm install
```

Then run in the background:

```bash
npx tailwindcss -i ./app/static/src/input.css -o ./app/static/dist/output.css --watch
```

Run the flask app:

```bash
uv run main.py
```

### Running with Uvicorn

To run the Flask app with Uvicorn, you can use the following command:

```bash
uvicorn main:app --reload
```

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Uv](https://github.com/astral-sh/uv)
- [Coding with Prince - Flask Dashboard](https://www.youtube.com/watch?v=SLftzEqoLPk&list=PLU7aW4OZeUzwn6L1txXQ9viaAIR2mDqbv)
- [Flowbite: Gettting Started/Flask](https://flowbite.com/docs/getting-started/flask/) - instruction on how to install Tailwind CSS Flask and Flowbite
- [Tailwind Flask Starter](https://github.com/themesberg/tailwind-flask-starter)
- [Chart.js](https://www.chartjs.org/docs/latest/getting-started/) -  it's a JavaScript library for creating interactive charts and graphs on the web.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

&copy; 2025 [Tomislav Dukez](https://github.com/tomdu3).
