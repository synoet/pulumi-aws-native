// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::RDS::OptionGroup resource creates an option group, to enable and configure features that are specific to a particular DB engine.
 */
export function getOptionGroup(args: GetOptionGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetOptionGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:rds:getOptionGroup", {
        "optionGroupName": args.optionGroupName,
    }, opts);
}

export interface GetOptionGroupArgs {
    /**
     * Specifies the name of the option group.
     */
    optionGroupName: string;
}

export interface GetOptionGroupResult {
    /**
     * Indicates what options are available in the option group.
     */
    readonly optionConfigurations?: outputs.rds.OptionGroupOptionConfiguration[];
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.rds.OptionGroupTag[];
}
/**
 * The AWS::RDS::OptionGroup resource creates an option group, to enable and configure features that are specific to a particular DB engine.
 */
export function getOptionGroupOutput(args: GetOptionGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetOptionGroupResult> {
    return pulumi.output(args).apply((a: any) => getOptionGroup(a, opts))
}

export interface GetOptionGroupOutputArgs {
    /**
     * Specifies the name of the option group.
     */
    optionGroupName: pulumi.Input<string>;
}
