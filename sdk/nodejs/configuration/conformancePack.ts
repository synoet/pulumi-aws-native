// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed as a single entity in an account and a region or across an entire AWS Organization.
 */
export class ConformancePack extends pulumi.CustomResource {
    /**
     * Get an existing ConformancePack resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ConformancePack {
        return new ConformancePack(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:configuration:ConformancePack';

    /**
     * Returns true if the given object is an instance of ConformancePack.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConformancePack {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConformancePack.__pulumiType;
    }

    /**
     * A list of ConformancePackInputParameter objects.
     */
    public readonly conformancePackInputParameters!: pulumi.Output<outputs.configuration.ConformancePackInputParameter[] | undefined>;
    /**
     * Name of the conformance pack which will be assigned as the unique identifier.
     */
    public readonly conformancePackName!: pulumi.Output<string>;
    /**
     * AWS Config stores intermediate files while processing conformance pack template.
     */
    public readonly deliveryS3Bucket!: pulumi.Output<string | undefined>;
    /**
     * The prefix for delivery S3 bucket.
     */
    public readonly deliveryS3KeyPrefix!: pulumi.Output<string | undefined>;
    /**
     * A string containing full conformance pack template body. You can only specify one of the template body or template S3Uri fields.
     */
    public readonly templateBody!: pulumi.Output<string | undefined>;
    /**
     * Location of file containing the template body which points to the conformance pack template that is located in an Amazon S3 bucket. You can only specify one of the template body or template S3Uri fields.
     */
    public readonly templateS3Uri!: pulumi.Output<string | undefined>;
    /**
     * The TemplateSSMDocumentDetails object contains the name of the SSM document and the version of the SSM document.
     */
    public readonly templateSsmDocumentDetails!: pulumi.Output<outputs.configuration.TemplateSsmDocumentDetailsProperties | undefined>;

    /**
     * Create a ConformancePack resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ConformancePackArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["conformancePackInputParameters"] = args ? args.conformancePackInputParameters : undefined;
            resourceInputs["conformancePackName"] = args ? args.conformancePackName : undefined;
            resourceInputs["deliveryS3Bucket"] = args ? args.deliveryS3Bucket : undefined;
            resourceInputs["deliveryS3KeyPrefix"] = args ? args.deliveryS3KeyPrefix : undefined;
            resourceInputs["templateBody"] = args ? args.templateBody : undefined;
            resourceInputs["templateS3Uri"] = args ? args.templateS3Uri : undefined;
            resourceInputs["templateSsmDocumentDetails"] = args ? args.templateSsmDocumentDetails : undefined;
        } else {
            resourceInputs["conformancePackInputParameters"] = undefined /*out*/;
            resourceInputs["conformancePackName"] = undefined /*out*/;
            resourceInputs["deliveryS3Bucket"] = undefined /*out*/;
            resourceInputs["deliveryS3KeyPrefix"] = undefined /*out*/;
            resourceInputs["templateBody"] = undefined /*out*/;
            resourceInputs["templateS3Uri"] = undefined /*out*/;
            resourceInputs["templateSsmDocumentDetails"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["conformancePackName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ConformancePack.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ConformancePack resource.
 */
export interface ConformancePackArgs {
    /**
     * A list of ConformancePackInputParameter objects.
     */
    conformancePackInputParameters?: pulumi.Input<pulumi.Input<inputs.configuration.ConformancePackInputParameterArgs>[]>;
    /**
     * Name of the conformance pack which will be assigned as the unique identifier.
     */
    conformancePackName?: pulumi.Input<string>;
    /**
     * AWS Config stores intermediate files while processing conformance pack template.
     */
    deliveryS3Bucket?: pulumi.Input<string>;
    /**
     * The prefix for delivery S3 bucket.
     */
    deliveryS3KeyPrefix?: pulumi.Input<string>;
    /**
     * A string containing full conformance pack template body. You can only specify one of the template body or template S3Uri fields.
     */
    templateBody?: pulumi.Input<string>;
    /**
     * Location of file containing the template body which points to the conformance pack template that is located in an Amazon S3 bucket. You can only specify one of the template body or template S3Uri fields.
     */
    templateS3Uri?: pulumi.Input<string>;
    /**
     * The TemplateSSMDocumentDetails object contains the name of the SSM document and the version of the SSM document.
     */
    templateSsmDocumentDetails?: pulumi.Input<inputs.configuration.TemplateSsmDocumentDetailsPropertiesArgs>;
}
