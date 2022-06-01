// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type Definition for AWS::ResilienceHub::App.
 */
export function getApp(args: GetAppArgs, opts?: pulumi.InvokeOptions): Promise<GetAppResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:resiliencehub:getApp", {
        "appArn": args.appArn,
    }, opts);
}

export interface GetAppArgs {
    /**
     * Amazon Resource Name (ARN) of the App.
     */
    appArn: string;
}

export interface GetAppResult {
    /**
     * Amazon Resource Name (ARN) of the App.
     */
    readonly appArn?: string;
    /**
     * Assessment execution schedule.
     */
    readonly appAssessmentSchedule?: enums.resiliencehub.AppAssessmentSchedule;
    /**
     * A string containing full ResilienceHub app template body.
     */
    readonly appTemplateBody?: string;
    /**
     * App description.
     */
    readonly description?: string;
    /**
     * Amazon Resource Name (ARN) of the Resiliency Policy.
     */
    readonly resiliencyPolicyArn?: string;
    /**
     * An array of ResourceMapping objects.
     */
    readonly resourceMappings?: outputs.resiliencehub.AppResourceMapping[];
    readonly tags?: outputs.resiliencehub.AppTagMap;
}

export function getAppOutput(args: GetAppOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAppResult> {
    return pulumi.output(args).apply(a => getApp(a, opts))
}

export interface GetAppOutputArgs {
    /**
     * Amazon Resource Name (ARN) of the App.
     */
    appArn: pulumi.Input<string>;
}
