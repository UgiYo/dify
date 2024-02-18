import type { FC } from 'react'
import BasePanel from '../_base/panel'

const Panel: FC = () => {
  return (
    <BasePanel
      inputsElement={<div>start panel inputs</div>}
      outputsElement={<div>start panel outputs</div>}
    />
  )
}

export default Panel