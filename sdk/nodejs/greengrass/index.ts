// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./connectorDefinition";
export * from "./connectorDefinitionVersion";
export * from "./coreDefinition";
export * from "./coreDefinitionVersion";
export * from "./deviceDefinition";
export * from "./deviceDefinitionVersion";
export * from "./functionDefinition";
export * from "./functionDefinitionVersion";
export * from "./group";
export * from "./groupVersion";
export * from "./loggerDefinition";
export * from "./loggerDefinitionVersion";
export * from "./resourceDefinition";
export * from "./resourceDefinitionVersion";
export * from "./subscriptionDefinition";
export * from "./subscriptionDefinitionVersion";

// Import resources to register:
import { ConnectorDefinition } from "./connectorDefinition";
import { ConnectorDefinitionVersion } from "./connectorDefinitionVersion";
import { CoreDefinition } from "./coreDefinition";
import { CoreDefinitionVersion } from "./coreDefinitionVersion";
import { DeviceDefinition } from "./deviceDefinition";
import { DeviceDefinitionVersion } from "./deviceDefinitionVersion";
import { FunctionDefinition } from "./functionDefinition";
import { FunctionDefinitionVersion } from "./functionDefinitionVersion";
import { Group } from "./group";
import { GroupVersion } from "./groupVersion";
import { LoggerDefinition } from "./loggerDefinition";
import { LoggerDefinitionVersion } from "./loggerDefinitionVersion";
import { ResourceDefinition } from "./resourceDefinition";
import { ResourceDefinitionVersion } from "./resourceDefinitionVersion";
import { SubscriptionDefinition } from "./subscriptionDefinition";
import { SubscriptionDefinitionVersion } from "./subscriptionDefinitionVersion";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "cloudformation:Greengrass:ConnectorDefinition":
                return new ConnectorDefinition(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:ConnectorDefinitionVersion":
                return new ConnectorDefinitionVersion(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:CoreDefinition":
                return new CoreDefinition(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:CoreDefinitionVersion":
                return new CoreDefinitionVersion(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:DeviceDefinition":
                return new DeviceDefinition(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:DeviceDefinitionVersion":
                return new DeviceDefinitionVersion(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:FunctionDefinition":
                return new FunctionDefinition(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:FunctionDefinitionVersion":
                return new FunctionDefinitionVersion(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:Group":
                return new Group(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:GroupVersion":
                return new GroupVersion(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:LoggerDefinition":
                return new LoggerDefinition(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:LoggerDefinitionVersion":
                return new LoggerDefinitionVersion(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:ResourceDefinition":
                return new ResourceDefinition(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:ResourceDefinitionVersion":
                return new ResourceDefinitionVersion(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:SubscriptionDefinition":
                return new SubscriptionDefinition(name, <any>undefined, { urn })
            case "cloudformation:Greengrass:SubscriptionDefinitionVersion":
                return new SubscriptionDefinitionVersion(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("cloudformation", "Greengrass", _module)