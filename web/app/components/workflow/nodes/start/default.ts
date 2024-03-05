import type { NodeDefault } from '../../types'
import type { StartNodeType } from './types'

const nodeDefault: NodeDefault<StartNodeType> = {
  defaultValue: {
    variables: [],
  },
  getAvailablePrevNodes() {
    return []
  },
  getAvailableNextNodes() {
    return []
  },
}

export default nodeDefault
