import type { ReactNode, FC } from "react";

interface PageProps {
  children: ReactNode | string;
}

const PageWrapper: FC<PageProps> = ({ children }) => {
  return (
    <main className="flex flex-col items-center justify-between min-h-screen p-24">
      {children}
    </main>
  );
};

export default PageWrapper;
