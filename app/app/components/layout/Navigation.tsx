import { usePathname } from "next/navigation";
import Link from "next/link";
import {
  Navbar,
  Center,
  Tooltip,
  UnstyledButton,
  createStyles,
  Stack,
  rem,
} from "@mantine/core";
import {
  IconHome2,
  IconLogout,
  IconDatabaseCog,
  IconBuildingWarehouse,
} from "@tabler/icons-react";

const useStyles = createStyles((theme) => ({
  link: {
    width: rem(50),
    height: rem(50),
    borderRadius: theme.radius.md,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[0]
        : theme.colors.gray[7],

    "&:hover": {
      backgroundColor:
        theme.colorScheme === "dark"
          ? theme.colors.dark[5]
          : theme.colors.gray[0],
    },
  },

  active: {
    "&, &:hover": {
      backgroundColor: theme.fn.variant({
        variant: "light",
        color: theme.primaryColor,
      }).background,
      color: theme.fn.variant({ variant: "light", color: theme.primaryColor })
        .color,
    },
  },
}));

interface NavbarLinkProps {
  icon: React.FC<any>;
  href?: string;
  label: string;
  active?: boolean;
  onClick?(): void;
}

function NavbarLink({
  icon: Icon,
  label,
  href,
  active,
  onClick,
}: NavbarLinkProps) {
  const { classes, cx } = useStyles();
  return (
    <Tooltip label={label} position="right" transitionProps={{ duration: 0 }}>
      <Link href={href || "/"}>
        <UnstyledButton
          onClick={onClick}
          className={cx(classes.link, { [classes.active]: active })}
        >
          <Icon size="1.2rem" stroke={1.5} />
        </UnstyledButton>
      </Link>
    </Tooltip>
  );
}

const navigationLinksTop = [
  { icon: IconHome2, label: "Home", href: "/" },
  { icon: IconBuildingWarehouse, label: "Food Storage", href: "/food-storage" },
];

const navigationLinksBottom = [
  { icon: IconDatabaseCog, label: "Developer Zone", href: "/dev-tools" },
  { icon: IconLogout, label: "Logout" },
];

const links = (link: any[], path: string) =>
  link.map((link, i) => (
    <NavbarLink {...link} key={i} active={link.href === path} />
  ));

export default function NavbarMinimal() {
  const path = usePathname();

  return (
    <Navbar width={{ base: 80 }} p="md">
      <Navbar.Section grow>
        <Stack justify="center" spacing={0}>
          {links(navigationLinksTop, path)}
        </Stack>
      </Navbar.Section>
      <Navbar.Section>
        <Stack justify="center" spacing={0}>
          {links(navigationLinksBottom, path)}
        </Stack>
      </Navbar.Section>
    </Navbar>
  );
}
