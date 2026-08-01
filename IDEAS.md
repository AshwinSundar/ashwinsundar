# IDEAS

## Photo Gallery

- inspo: https://freefrontend.com/css-gallery/

### Features

- Option 1: tiled gallery of images
    - i'll tile them manually and design each album
    - create a template like this: https://freefrontend.com/css-gallery/#2026-01-01-responsive-css-grid-mosaic-gallery-l
    - look for a simple solution to responsive design (i like what the above example does)
- load a small rendering on `reveal`
    - example: https://freefrontend.com/css-gallery/#2026-03-12-css-has-character-select-screen-l
- load the thumbnail immediately after
- on `mousedown`, preload the full image
- show the full image in a fullscreen dialog
    - blur, dim and greyscale the background
- cache all the endpoints

- Option 2: KISS 
    - https://freefrontend.com/css-gallery/page/2/#2025-11-21-pure-html-css-image-slideshow-l
    - pure HTML and CSS
    - i like this. start here, then add more refinement as needed


-- 

aight i went with option 2. i created an albums.json that will hold metadata about each photo album. then there is a load_photos function that will use Pillow to load images into a nice object. Finally, there is an albums endpoint that will return a template displaying the album.


