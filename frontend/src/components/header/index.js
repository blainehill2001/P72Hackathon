import { h } from "preact";
import { Link } from "preact-router/match";
import style from "./style.css";
import githubIcon from "../../assets/github-icon.svg";

const Header = () => (
  <header class={style.header}>
    <a href="https://itinerfy.vercel.app/" class={style.logo}>
      <h1>Itinerfy</h1>
    </a>
    <nav class={style.navContainer}>
      <a
        href="https://github.com/blainehill2001/P72Hackathon"
        class={style.githubLink}
      >
        <img
          src={githubIcon}
          alt="GitHub Icon"
          height="32"
          width="32"
          class={style.githubIcon}
        />
      </a>
    </nav>
  </header>
);

export default Header;
