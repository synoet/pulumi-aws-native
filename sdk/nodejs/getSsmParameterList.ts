// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "./types";
import * as utilities from "./utilities";

export function getSsmParameterList(args: GetSsmParameterListArgs, opts?: pulumi.InvokeOptions): Promise<GetSsmParameterListResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("aws-native:index:getSsmParameterList", {
        "name": args.name,
    }, opts);
}

export interface GetSsmParameterListArgs {
    name: string;
}

export interface GetSsmParameterListResult {
    readonly value: string[];
}
