---
title: ""
hide:
---
# Image Analysis Packages

Some of the image processing we do in cryo-EM is domain specific. 

These packages for image analysis help you to explore your new ideas without reinventing the wheel. 
Many are implemented in PyTorch, this means they can run on GPUs and make use of autodiff
for parameter optimisation.

<div class="grid cards" markdown>
-   :fontawesome-regular-file-lines:{ .lg .middle } [__torch-fourier-slice__](https://github.com/teamtomo/torch-fourier-slice) [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-fourier-slice) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-fourier-slice)

    ---

    _Fourier slice extraction/insertion_

-   :material-rhombus-split-outline:{ .lg .middle } [__torch-cubic-spline-grids__](https://github.com/teamtomo/torch-cubic-spline-grids) [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-cubic-spline-grids) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-cubic-spline-grids)

    ---

    _Cubic spline interpolation on regular grids_

-   :material-magnify-scan:{ .lg .middle } [__torch-fourier-rescale__](https://github.com/teamtomo/torch-fourier-rescale) [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-fourier-rescale) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-fourier-rescale)

    ---

    _Fast and accurate image rescaling using Fourier methods_

-   :material-arrow-all:{ .lg .middle } [__torch-fourier-shift__](https://github.com/teamtomo/torch-fourier-shift) [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-fourier-shift) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-fourier-shift)

    ---

    _Subpixel image shifting using Fourier transforms_

-   :material-crop:{ .lg .middle } [__torch-subpixel-crop__](https://github.com/teamtomo/torch-subpixel-crop) [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-subpixel-crop) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-subpixel-crop)

    ---

    _Accurate subpixel cropping for image processing_

-   :material-grid-off:{ .lg .middle } [__torch-image-lerp__](https://github.com/teamtomo/torch-image-lerp) [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-image-lerp) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-image-lerp)

    ---

    _Sample and insert values in images and volumes_

-   :material-grid:{ .lg .middle } [__torch-grid-utils__](https://github.com/teamtomo/torch-grid-utils) [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-grid-utils) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-grid-utils)

    ---

    _Utilities for working with real-space and fourier-space grids_

-   :material-contactless-payment:{ .lg .middle } [__torch-fourier-shell-correlation__](https://github.com/teamtomo/torch-fourier-shell-correlation) [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-fourier-shell-correlation) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-fourier-shell-correlation)

    ---

    _FSC calculation for resolution estimation_

-   :material-refresh:{ .lg .middle } [__torch-so3__](https://github.com/teamtomo/torch-so3) [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-so3) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-so3)

    ---

    _3D rotation operations and utilities_

-   :material-align-horizontal-left:{ .lg .middle } [__torch-tiltxcorr__](https://github.com/teamtomo/torch-tiltxcorr) [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-tiltxcorr) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-tiltxcorr)

    ---

    _Coarse tilt series alignment_

-   :material-rotate-3d:{ .lg .middle } [__torch-transform-image__](https://github.com/teamtomo/torch-transform-image) [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-transform-image) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-transform-image)

    ---

    _Real space transformations of 2D/3D images_

-   :material-chart-bell-curve:{ .lg .middle } [__torch-find-peaks__](https://github.com/teamtomo/torch-find-peaks) [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-find-peaks) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-find-peaks)

    ---

    _Find and refine peaks in 2D/3D images_

-   :material-matrix:{ .lg .middle } [__torch-affine-utils__](https://github.com/teamtomo/torch-affine-utils) [:fontawesome-solid-book:{ .middle }](https://teamtomo.org/torch-affine-utils) [:fontawesome-brands-github:{ .middle }](https://github.com/teamtomo/torch-affine-utils)

    ---

    _Utilities for affine transforms of 2D/3D coordinates_
</div>

