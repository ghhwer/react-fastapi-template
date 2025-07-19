'use client';
import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import Link from 'next/link'

import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { 
  faSatellite, faRocket, 
  faDashboard, faCog, 
  faDoorOpen
 } from '@fortawesome/free-solid-svg-icons';
import { usePathname } from 'next/navigation';
import { useEffect, useState } from 'react';

interface SidebarItem {
  url: string;
  icon: any;
  active: boolean;
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const [theme, setTheme] = useState('dark'); // or 'light'

  //useEffect(() => {
  //  const storedTheme = localStorage.getItem('theme');
  //  if (storedTheme) {
  //    setTheme(storedTheme);
  //  }
  //}, []);

  const pathname = usePathname();
  const applicationName = "Example Application";

  const sidebarItems: SidebarItem[] = [
    { url: '/', icon: faDashboard },
    { url: '/pageA', icon: faSatellite },
    { url: '/pageB', icon: faRocket },
    { url: '/settings', icon: faCog },
    // Add more items as needed
  ].map(item => ({ ...item, active: pathname === item.url }));

  useEffect(() => {
    const title = pathname === '/' ? 'Dashboard' : pathname.substring(1).charAt(0).toUpperCase() + pathname.substring(2);
    document.title = title;
  }, [pathname]);


  return (
    <html data-theme={theme}>
      <body className="bg-white dark:bg-black text">
        <div className="flex flex-col h-screen">
          <header className="bg text p-4 flex justify-between items-center">
            <h1 className="text-lg font-bold">{applicationName}</h1>
          </header>
          <div className="flex flex-1">
            <aside id="sidebar" className="bg w-16 overflow-y-auto transition-width duration-300">
              <div className="justify-items-center">
                {sidebarItems.map((item, index) => (
                  <div key={index} className="mt-4">
                    <Link
                      href={item.url}
                      className={
                        `${item.active ? 'text-gray-600/100 dark:text-gray-100/100' :
                          'text-gray-600/100 dark:text-gray-400/100 hover:text-gray-600/100 dark:hover:text-gray-200/100'
                        }`}>
                      <span className="inline-block w-6">
                        <FontAwesomeIcon icon={item.icon} className="fa-lg" />
                      </span>
                    </Link>
                  </div>
                ))}
                <div className="mt-4">
                  <Link href="/logout"
                    className='text-gray-600/100 dark:text-gray-400/100 hover:text-gray-600/100 dark:hover:text-gray-200/100'>
                    <span className="inline-block w-6">
                      <FontAwesomeIcon icon={faDoorOpen} className="fa-lg" />
                    </span>
                  </Link>
                </div>
              </div>
            </aside>
            {children}
          </div>
          <footer className="bg text pb-2">
          </footer>
        </div>
      </body>
    </html>
  );
}
