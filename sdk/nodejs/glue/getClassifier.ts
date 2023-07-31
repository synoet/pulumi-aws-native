// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Glue::Classifier
 */
export function getClassifier(args: GetClassifierArgs, opts?: pulumi.InvokeOptions): Promise<GetClassifierResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:glue:getClassifier", {
        "id": args.id,
    }, opts);
}

export interface GetClassifierArgs {
    id: string;
}

export interface GetClassifierResult {
    readonly csvClassifier?: outputs.glue.ClassifierCsvClassifier;
    readonly grokClassifier?: outputs.glue.ClassifierGrokClassifier;
    readonly id?: string;
    readonly jsonClassifier?: outputs.glue.ClassifierJsonClassifier;
    readonly xmlClassifier?: outputs.glue.ClassifierXMLClassifier;
}
/**
 * Resource Type definition for AWS::Glue::Classifier
 */
export function getClassifierOutput(args: GetClassifierOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetClassifierResult> {
    return pulumi.output(args).apply((a: any) => getClassifier(a, opts))
}

export interface GetClassifierOutputArgs {
    id: pulumi.Input<string>;
}
