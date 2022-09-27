import React, { ReactNode } from 'react'
import Navigation from './core/nav'

type Props = {
   children: ReactNode
}

const Layout = (props: Props) => {
  return (
    <div>
      <Navigation />
      {props.children}
    </div>
  )
}

export default Layout