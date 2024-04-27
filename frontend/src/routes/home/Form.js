import { useState, useEffect } from "preact/hooks";

const Form = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [currentTime, setCurrentTime] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Name:", name);
    console.log("Email:", email);
    fetch("http://localhost:5000/algo")
      .then((response) => response.text())
      .then((data) => setCurrentTime(data));
  };

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_API_URL || "http://127.0.0.1:5000";
    fetch(`${apiUrl}/get_time`, {
      method: "GET",
    })
      .then((response) => response.text())
      .then((data) => setCurrentTime(data));
  }, []);

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>
        <label>
          Email:
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>
        <button type="submit">Submit</button>
      </form>
      <p>Current Time: {currentTime}</p>
    </div>
  );
};

export default Form;
