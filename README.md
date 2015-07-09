# Osoba

Osoba is OCCRP's graph database, intended to keep track of people, companies,
and all sorts of other things around the world, from numerous data sources.

## Specifications

See `doc/specs.md`

## Dependencies

Osoba is written in Python with Flask. All Python requirements are specified
in `requirements.txt`.

Osoba requires a PostgreSQL database.

## Running

The simplest way to run is to use Docker. Try:

```
$ docker build . --tag osoba
$ docker run -a -i --name osoba --link=postgres-osoba:postgres-osoba osoba
```

To run in detached mode, replace `-a -i` with `-d`.

To run in development mode (where the system restarts on source changes),
add `--volume=/path/to/osoba/source:/usr/src/osoba/`.

## Testing

No testing exists yet. Bad Smári!
