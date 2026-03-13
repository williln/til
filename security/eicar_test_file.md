# The EICAR Test File

## Links

- [EICAR test file - Wikipedia](https://en.wikipedia.org/wiki/EICAR_test_file)
- [EICAR (European Institute for Computer Antivirus Research)](https://www.eicar.org/)

## Use case

You want to test whether virus/malware scanning is working in your system (e.g., file upload pipelines, cloud storage, API integrations) without using an actual virus.

## What is EICAR?

**EICAR** stands for the **European Institute for Computer Antivirus Research**. They created a standardized test file that antivirus software recognizes as "malicious" — but it's completely harmless. It's just a specific string of printable ASCII characters.

## The test string

The EICAR test string is:

```
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
```

Save it as a file (e.g., `eicar-test.txt`) and your antivirus software should flag it.

## What happens in practice

- **Local machine**: Your OS may quarantine the file automatically — but not always. My Mac did not quarantine it.
- **API/cloud storage**: When I uploaded the file through an API, the upload itself succeeded. However, when I tried to **access** the uploaded resource, I got an **"access denied"** error. This suggests the virus scanning happened asynchronously — the file was accepted on upload but flagged and blocked before it could be served.

## Why this is useful

- Validates that your virus scanning pipeline is actually working end-to-end
- Safe to use — it's not a real virus, just a string that AV software agrees to flag
- Helps you understand **where** in the pipeline scanning happens (upload time vs. access time)
- Good for testing error handling when a file is flagged
