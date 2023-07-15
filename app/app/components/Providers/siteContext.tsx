"use client";
import { createContext, useState, useContext } from "react";
import type { ReactNode, Dispatch } from "react";

type SiteContextType = {
  test?: string;
  controlBar?: ReactNode;
  setControlBar?: Dispatch<ReactNode>;
};

const SiteContext = createContext<SiteContextType>({});

interface ContextProviderProps {
  children: ReactNode;
}

export const ContextProvider = ({ children }: ContextProviderProps) => {
  const [controlBar, setControlBar] = useState<ReactNode>(null);

  const value = {
    controlBar,
    setControlBar,
    test: "hello world",
  };

  return <SiteContext.Provider value={value}>{children}</SiteContext.Provider>;
};

export const useSite = () => useContext(SiteContext);
