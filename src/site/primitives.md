---
title: ""
---
# Image Analysis Primitives

These packages for image analysis help you to explore your new ideas without reinventing the wheel. 
Packages are implemented in PyTorch, this means they can run on GPUs and make use of autodiff
for parameter optimisation.

### Fourier Space
- :fontawesome-regular-file-lines: **torch-fourier-slice** | extracting/inserting central slices of Fourier transforms | [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-fourier-slice) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-fourier-slice)
- :material-magnify-scan: **torch-fourier-rescale** | rescale by padding/cropping Fourier transforms | [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-fourier-rescale) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-fourier-rescale)
- :material-arrow-all: **torch-fourier-shift** | subpixel shift by phase shifting Fourier transforms | [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-fourier-shift) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-fourier-shift)
- :material-tune: **torch-fourier-filter** | Fourier space filters (including the CTF) | [:fontawesome-solid-book:{ .middle }](https://github.com/teamtomo/torch-fourier-filter) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-fourier-filter)
- :material-contactless-payment:**torch-fourier-shell-correlation** | correlation as a function of spatial frequency | [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-fourier-shell-correlation) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-fourier-shell-correlation)

### Real Space
- :material-grid-off: **torch-image-interpolation** | sample values from or insert values into images | [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-image-interpolation) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-image-interpolation)
- :material-rotate-3d: **torch-transform-image** | affine transforms of images  |  [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-transform-image) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-transform-image)
- :material-rhombus-split-outline: **torch-cubic-spline-grids** | continuous parametrisations of 1-4D spaces | [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-cubic-spline-grids) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-cubic-spline-grids)
- :material-crop: **torch-subpixel-crop** | crop from images with subpixel precision | [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-subpixel-crop) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-subpixel-crop)
- :material-chart-bell-curve: **torch-find-peaks** | find and refine peaks in images | [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-find-peaks) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-find-peaks)

### Utilities
- :material-grid:**torch-grid-utils** | coordinate grids, frequency grids and shape generation | [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-grid-utils) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-grid-utils)
- :material-refresh:**torch-so3** | 3D rotation operations and utilities | [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-so3) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-so3)
- :material-matrix:**torch-affine-utils** | affine matrix generation for 2D/3D coordinates | [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-affine-utils) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-affine-utils)




