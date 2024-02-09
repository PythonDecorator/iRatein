import { Box } from '@mui/system';
import CssBaseline from '@mui/material/CssBaseline';

import PrimaryAppBar from "./includes/PrimaryAppBar"
import PrimaryDraw from "./includes/PrimaryDraw"


const Home = () => {
    return (
      <Box sx={{display: "flex"}}>
          <CssBaseline/>
          <PrimaryAppBar/>
          <PrimaryDraw>
          </PrimaryDraw>
      </Box>
    );
  }

export default Home;