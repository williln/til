# Run SQL statements as part of your migrations with `migrations.RunSQL` 

## Links 

- [RunSQL](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#runsql)

## Notes 

`migrations.RunSQL` enables you to run raw SQL on your database from within your migration file. 

From the docs: 

You can also pass a list of strings or 2-tuples. The latter is used for passing queries and parameters in the same way as cursor.execute(). These three operations are equivalent:

```py
migrations.RunSQL("INSERT INTO musician (name) VALUES ('Reinhardt');")
migrations.RunSQL([("INSERT INTO musician (name) VALUES ('Reinhardt');", None)])
migrations.RunSQL([("INSERT INTO musician (name) VALUES (%s);", ["Reinhardt"])])
```

> I haven't used this myself, but learned about it from someone else and wanted to document it! 
