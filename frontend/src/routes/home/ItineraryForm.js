import { useState } from "preact/hooks";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import IconButton from "@mui/material/IconButton";
import DeleteIcon from "@mui/icons-material/Delete";

const ItineraryForm = () => {
  const [locations, setLocations] = useState([]);
  const [newLocation, setNewLocation] = useState("");
  const [priority, setPriority] = useState(3);
  const [visitTime, setVisitTime] = useState("");
  const [apiResponse, setApiResponse] = useState(null);

  const handleAddLocation = () => {
    const locationData = {
      name: newLocation,
      priority: priority,
      time: visitTime || undefined,
    };
    setLocations([...locations, locationData]);
    setNewLocation("");
    setPriority(3);
    setVisitTime("");
  };

  const handleRemoveLocation = (index) => {
    const updatedLocations = locations.filter((_, idx) => idx !== index);
    setLocations(updatedLocations);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const apiUrl = "http://127.0.0.1:5000/algo";
    fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ locations }),
    })
      .then((response) => response.json())
      .then((data) => {
        setApiResponse(data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Location"
          variant="outlined"
          value={newLocation}
          onChange={(e) => setNewLocation(e.target.value)}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Priority (1-5)"
          type="number"
          InputProps={{ inputProps: { min: 1, max: 5 } }}
          value={priority}
          onChange={(e) => setPriority(parseInt(e.target.value))}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Visit Time (optional)"
          type="time"
          value={visitTime}
          onChange={(e) => setVisitTime(e.target.value)}
          fullWidth
          margin="normal"
        />
        <Button
          variant="contained"
          onClick={handleAddLocation}
          style={{ margin: 8 }}
        >
          Add Location
        </Button>
        <Button type="submit" variant="contained" color="primary">
          Submit Itinerary
        </Button>
      </form>
      <List>
        {locations.map((loc, index) => (
          <ListItem
            key={index}
            secondaryAction={
              <IconButton
                edge="end"
                aria-label="delete"
                onClick={() => handleRemoveLocation(index)}
              >
                <DeleteIcon />
              </IconButton>
            }
          >
            <ListItemText
              primary={loc.name}
              secondary={`Priority: ${loc.priority} - Time: ${
                loc.time || "Anytime"
              }`}
            />
          </ListItem>
        ))}
      </List>
      {apiResponse && <div>Response: {JSON.stringify(apiResponse)}</div>}
    </div>
  );
};

export default ItineraryForm;
