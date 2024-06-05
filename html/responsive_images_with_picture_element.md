# Creating responsive images with `srcset`, `sizes`, and `<picture>` 

## Links 

- [Responsive images - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images). This article is very clear and uses lots of examples. 

Thanks to my colleague [Jeff Triplett](https://webology.dev/) for sharing this article with me. 

## Quick explanation 

**Art direction problem** is when you want to use completely different image files (a cropped version that focuses on a face for a thumbnail, for example) with different screen sizes

> A second cropped image could be displayed for a medium-width screen device, like a tablet. The general problem whereby you want to serve different cropped images in that way, for various layouts, is commonly known as the art direction problem.

**Resolution-switching problem** is when you want to use a lower-resolution image on smaller screens.

> [m]obile users don't want to waste bandwidth by downloading a large image intended for desktop users, when a small image would do for their device. Conversely, a small raster image starts to look grainy when displayedlargerthanitsoriginalsize(arasterimage is a set number of pixels wide and a set number of pixels tall, as we saw when we looked at vector graphics). Ideally, multiple resolutions would bemadeavailabletotheuser'swebbrowser. Thebrowser could then determine the optimal resolution to load based on the screen size of the user's device. This is called the resolution switching problem.

## `srcset` and `sizes` 

> `srcset` defines the set of images we will allow the browser to choose between, and what size each image is. Each set of image information is separated from the previous one by a comma.

> `sizes` defines a set of media conditions (e.g. screen widths) and indicates what image size would be best to choose, when certain media conditions are true

- A **media condition** is another phrase for screen "state" (screen size, pixel density, zoom level, screen orientation, and network speed)

---

### Resolution switching: different sizes 

[Source](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images#resolution_switching_different_sizes)

```html
<img
  srcset="elva-fairy-480w.jpg 480w, elva-fairy-800w.jpg 800w"
  sizes="(max-width: 600px) 480px,
         800px"
  src="elva-fairy-800w.jpg"
  alt="Elva dressed as a fairy" />
```

Note the `sizes` element being passed, and the size in `srcset` after each value to correspond. 

---

### Resolution switching: same size, different resolutions 

[Source](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images#resolution_switching_same_size_different_resolutions)

```html
<img
  srcset="elva-fairy-320w.jpg, elva-fairy-480w.jpg 1.5x, elva-fairy-640w.jpg 2x"
  src="elva-fairy-640w.jpg"
  alt="Elva dressed as a fairy" />
```

Note the `1.5x` and `2x` with the second and third `srcset` values. 

---

### Art direction: use a different image for a different display 

[Source](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images#art_direction)

```html
<picture>
  <source media="(max-width: 799px)" srcset="elva-480w-close-portrait.jpg" />
  <source media="(min-width: 800px)" srcset="elva-800w.jpg" />
  <img src="elva-800w.jpg" alt="Chris standing up holding his daughter Elva" />
</picture>

```
