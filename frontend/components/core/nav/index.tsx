import React from "react";
import Link from "next/link";

type Props = {};

const Navigation = (props: Props) => {
  const linkList = [
    {
      name: "Home",
      href: "/",
    },
    {
      name: "OTE",
      href: "/ote",
    },
    {
      name: "ERU",
      href: "/eru",
    },
  ];

  return (
    <nav>
      {linkList.map((link) => (
        <Link key={link.name} href={link.href}>
          <a>{link.name}</a>
        </Link>
      ))}
    </nav>
  );
};

export default Navigation;
