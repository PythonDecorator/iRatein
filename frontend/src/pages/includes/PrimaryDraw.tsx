import {Box, Drawer, Typography} from "@mui/material"
import { useMediaQuery } from "@mui/material/index";
import { useTheme } from '@mui/material/styles';
import { useEffect, useState, ReactNode } from "react";
import DrawerToggle from "../../components/PrimaryDraw/DrawToggle";
import React from "react";

type Props = {
    children: ReactNode;
};

type ChildProps = {
    open: Boolean;
};

type ChildElement = React.ReactElement<ChildProps>;

const PrimaryDraw: React.FC<Props> = ({ children }) => {
    const theme = useTheme();
    const below600 =  useMediaQuery("(max-width:599px)");
    const [open, setOpen] = useState(true)

    useEffect(() => {
        setOpen(!below600);
    }, [below600]);

     const handleDrawerOpen = () => {
        setOpen(true);
     };

     const handleDrawerClose = () => {
        setOpen(false);
     };

    return (
    <Drawer
    open={open}
    variant={below600 ? "temporary" : "permanent"}
    PaperProps={{
        sx: {
            mt: `${theme.primaryAppBar.height}px`,
            height: `calc(100vh - ${theme.primaryAppBar.height}px )`,
            width: theme.primaryDraw.width,
        },
    }}
    >
      <Box>
        <Box sx={{
            position: "absolute",
            top: 0,
            right: 0,
            width: open ? "auto" : "100",
        }}>
            <DrawerToggle
            open={open}
            handleDrawerClose={handleDrawerClose}
            handleDrawerOpen={handleDrawerOpen}
            />

            {React.Children.map(children, (child) => {
                return React.isValidElement(child)
                ? React.cloneElement(child as ChildElement, { open })
                : child;
            })}
        </Box>
      </Box>
    </Drawer>
)};

export default PrimaryDraw;