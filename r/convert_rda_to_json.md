# How to convert an `.rda` file to JSON 

- Homebrew 
- RStudio 

1. Install R and [RStudio]((https://www.rstudio.com/products/rstudio/download/))

```sh
brew install R
brew install -cask rstudio
```

2. Launch RStudio.

```sh
open -a RStudio
```

This opens a new application. Stay on the Console tab -- does what it says on the tin 

<img width="1193" alt="Screenshot 2023-04-21 at 12 47 09 AM" src="https://user-images.githubusercontent.com/2286304/233575564-73880250-8455-476b-a048-d4d5f87fa411.png">

The rest of the commands should be run in Rstudio 

3. Install the jsonlite package (if not already installed). 

```sh
install.packages("jsonlite")
```

4. Load the .rda file:

In the console: 

```sh
load("path/to/your/file.rda")
```

Or in the Rstudio UI: 

<img width="566" alt="Screenshot 2023-04-21 at 12 49 28 AM" src="https://user-images.githubusercontent.com/2286304/233576220-44566fe9-1a74-494a-944a-ca0fc0132d5c.png">
<img width="282" alt="Screenshot 2023-04-21 at 12 49 36 AM" src="https://user-images.githubusercontent.com/2286304/233576222-8e843d69-ce16-495d-9172-1c03892119ef.png">

5. Check the loaded object(s) by running:

```sh
ls()
```

6. Convert the loaded object to JSON and save it to your desired location (in this example, the Desktop folder):

```sh
jsonlite::write_json(loaded_object, "~/Desktop/output_file.json")
```

Replace loaded_object with the name of the object you want to convert, as obtained from the `ls()` command.

Result: 

<img width="1678" alt="Screenshot 2023-04-21 at 12 51 54 AM" src="https://user-images.githubusercontent.com/2286304/233576717-a33b64a1-e142-4b2a-a10a-3c04e9bef614.png">
