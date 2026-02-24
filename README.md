<a id="readme-top"></a>


<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/PensiveEagle">
    <img src="https://raw.githubusercontent.com/PensiveEagle/asset-repo/822e4442213f8046000d4c47cec31e4112dac30b/readme_assets/general_assets/pensiveeagle-logo-green.svg" alt="Pensive Eagle Logo" width="200" height="auto">
  </a>

<h3 align="center">Astronomy Picture of the Day</h3>

  <p align="center">
    A simple dockerised application that displays the NASA Astronomy of the Day
    <br />
  <!--  <a href="https://github.com/PensiveEagle/astro-pic-app"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
  <!--  <a href="https://github.com/PensiveEagle/astro-pic-app">View Demo</a>
    &middot;
    <a href="https://github.com/PensiveEagle/astro-pic-app/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/PensiveEagle/astro-pic-app/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


<img src="/image/capture.png" alt="project_capture" width="100%" height="auto">

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][python-shield]][python-url]
[![Streamlit][streamlit-shield]][streamlit-url]
[![Docker][docker-shield]][docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* NASA API Key - This can be created for free at https://api.nasa.gov#signUp
* Docker

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/PensiveEagle/astro-pic-app.git
   ```
3. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin PensiveEagle/astro-pic-app
   git remote -v # confirm the changes
   ```
4. Create a ".env" file at the project root: `astro-pic-app/.env`
5. Enter your API in `.env`
   ```env
   NASA_API_KEY='Enter your api key'
   ```
6. Build the docker image
   ```sh
   docker build -t astro-pic-app .
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Running the docker image
To run the application you will need to run the docker image built during the installation steps
```sh
docker run --rm -d --name astro-pic-app-1 -p 8080:8080 --env-file ./.env astro-pic-app
```

You should then be able to access the app in your browser at http://localhost:8080



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<div align="center"><img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/869e68466915785fdc1c44c324f2d84de119e5f1/readme_assets/general_assets/makers_mark_circle.svg" width="50"></div>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/PensiveEagle/astro-pic-app.svg?style=for-the-badge
[contributors-url]: https://github.com/PensiveEagle/astro-pic-app/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PensiveEagle/astro-pic-app.svg?style=for-the-badge
[forks-url]: https://github.com/PensiveEagle/astro-pic-app/network/members
[stars-shield]: https://img.shields.io/github/stars/PensiveEagle/astro-pic-app.svg?style=for-the-badge
[stars-url]: https://github.com/PensiveEagle/astro-pic-app/stargazers
[issues-shield]: https://img.shields.io/github/issues/PensiveEagle/astro-pic-app.svg?style=for-the-badge
[issues-url]: https://github.com/PensiveEagle/astro-pic-app/issues
[license-shield]: https://img.shields.io/github/license/PensiveEagle/astro-pic-app.svg?style=for-the-badge
[license-url]: https://github.com/PensiveEagle/astro-pic-app/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jameshall-profile
[docker-shield]: https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/
[streamlit-shield]: https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[streamlit-url]: https://streamlit.io/
[python-shield]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.org/

