// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { BrokerArgs } from "./broker";
export type Broker = import("./broker").Broker;
export const Broker: typeof import("./broker").Broker = null as any;
utilities.lazyLoad(exports, ["Broker"], () => require("./broker"));

export { ConfigurationArgs } from "./configuration";
export type Configuration = import("./configuration").Configuration;
export const Configuration: typeof import("./configuration").Configuration = null as any;
utilities.lazyLoad(exports, ["Configuration"], () => require("./configuration"));

export { ConfigurationAssociationArgs } from "./configurationAssociation";
export type ConfigurationAssociation = import("./configurationAssociation").ConfigurationAssociation;
export const ConfigurationAssociation: typeof import("./configurationAssociation").ConfigurationAssociation = null as any;
utilities.lazyLoad(exports, ["ConfigurationAssociation"], () => require("./configurationAssociation"));

export { GetBrokerArgs, GetBrokerResult, GetBrokerOutputArgs } from "./getBroker";
export const getBroker: typeof import("./getBroker").getBroker = null as any;
export const getBrokerOutput: typeof import("./getBroker").getBrokerOutput = null as any;
utilities.lazyLoad(exports, ["getBroker","getBrokerOutput"], () => require("./getBroker"));

export { GetConfigurationArgs, GetConfigurationResult, GetConfigurationOutputArgs } from "./getConfiguration";
export const getConfiguration: typeof import("./getConfiguration").getConfiguration = null as any;
export const getConfigurationOutput: typeof import("./getConfiguration").getConfigurationOutput = null as any;
utilities.lazyLoad(exports, ["getConfiguration","getConfigurationOutput"], () => require("./getConfiguration"));

export { GetConfigurationAssociationArgs, GetConfigurationAssociationResult, GetConfigurationAssociationOutputArgs } from "./getConfigurationAssociation";
export const getConfigurationAssociation: typeof import("./getConfigurationAssociation").getConfigurationAssociation = null as any;
export const getConfigurationAssociationOutput: typeof import("./getConfigurationAssociation").getConfigurationAssociationOutput = null as any;
utilities.lazyLoad(exports, ["getConfigurationAssociation","getConfigurationAssociationOutput"], () => require("./getConfigurationAssociation"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:amazonmq:Broker":
                return new Broker(name, <any>undefined, { urn })
            case "aws-native:amazonmq:Configuration":
                return new Configuration(name, <any>undefined, { urn })
            case "aws-native:amazonmq:ConfigurationAssociation":
                return new ConfigurationAssociation(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "amazonmq", _module)
