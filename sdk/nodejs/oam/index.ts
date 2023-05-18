// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { GetLinkArgs, GetLinkResult, GetLinkOutputArgs } from "./getLink";
export const getLink: typeof import("./getLink").getLink = null as any;
export const getLinkOutput: typeof import("./getLink").getLinkOutput = null as any;
utilities.lazyLoad(exports, ["getLink","getLinkOutput"], () => require("./getLink"));

export { GetSinkArgs, GetSinkResult, GetSinkOutputArgs } from "./getSink";
export const getSink: typeof import("./getSink").getSink = null as any;
export const getSinkOutput: typeof import("./getSink").getSinkOutput = null as any;
utilities.lazyLoad(exports, ["getSink","getSinkOutput"], () => require("./getSink"));

export { LinkArgs } from "./link";
export type Link = import("./link").Link;
export const Link: typeof import("./link").Link = null as any;
utilities.lazyLoad(exports, ["Link"], () => require("./link"));

export { SinkArgs } from "./sink";
export type Sink = import("./sink").Sink;
export const Sink: typeof import("./sink").Sink = null as any;
utilities.lazyLoad(exports, ["Sink"], () => require("./sink"));


// Export enums:
export * from "../types/enums/oam";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:oam:Link":
                return new Link(name, <any>undefined, { urn })
            case "aws-native:oam:Sink":
                return new Sink(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "oam", _module)
