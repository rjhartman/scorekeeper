import type { FC } from "react";
import { Header, Group } from "@mantine/core";

interface NavigationProps {}

const Navigation: FC<NavigationProps> = () => {
  return (
    <Header height={60} p="xs">
      <Group sx={{ height: "100%" }} px={20} position="apart">
        <span>Logo</span>
      </Group>
    </Header>
  );
};

export default Navigation;
