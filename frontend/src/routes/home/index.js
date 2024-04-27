import { h } from "preact";
import style from "./style.css";
import ItineraryForm from "./ItineraryForm";

const Home = () => {
  return (
    <div class={style.home}>
      <ItineraryForm />
    </div>
  );
};

const Resource = (props) => {
  return (
    <a href={props.link} class={style.resource}>
      <h2>{props.title}</h2>
      <p>{props.description}</p>
    </a>
  );
};

export default Home;
