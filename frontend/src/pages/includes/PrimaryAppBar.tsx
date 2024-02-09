import { AppBar, Toolbar,
    Link, Typography, IconButton ,
    Drawer, useMediaQuery,
} from '@mui/material';
import { Box } from '@mui/material/index';
import { useTheme } from '@mui/material/styles';
import MenuIcon from "@mui/icons-material/Menu";
import {useState, useEffect} from "react"


const PrimaryAppBar = () => {
    const theme = useTheme();

    const [sideMenu, setSideMenu] = useState(false);

    const toggleDrawer = (open: boolean) => (
        event: React.MouseEvent) => {setSideMenu(open)};

    const isSmallScreen = useMediaQuery(theme.breakpoints.up("sm"));

    useEffect(() => {
        if (isSmallScreen && sideMenu) {
            setSideMenu(false);
        }
    }, [isSmallScreen]);

    return (
        <AppBar sx={{
            zIndex: (theme) => theme.zIndex.drawer + 2,
            backgroundColor: theme.palette.background.default,
            borderBottom: `1px solid ${theme.palette.divider}`
        }}>
            <Toolbar variant="dense" sx={{
                height: theme.primaryAppBar.height,
                minHeight: theme.primaryAppBar.height
            }}>
                <Box sx={{
                    display: {xs: "block", sm: "none"}
                }}>
                    <IconButton color="inherit"
                    arial-label="Open drawer"
                    edge="start" sx={{mr: 2}}
                    onClick={toggleDrawer(true)}
                    >
                      <MenuIcon />
                    </IconButton>
                </Box>

                <Drawer anchor="left" open={sideMenu} onClose={toggleDrawer(false)}>
                    {[...Array(100)].map((_, i) => (
                        <Typography>
                            {i + 1}
                        </Typography>
                    ))}
                </Drawer>

                <Link href="/" underline="none" color="inherit">
                    <Typography
                    varient="h6"
                    noWrap
                    component="div"
                    sx={{display: { fontWeight: 700, letterSpace: "-0.05px"} }}>iRatein</Typography>
                </Link>
            </Toolbar>
        </AppBar>
    )
};


export default PrimaryAppBar;