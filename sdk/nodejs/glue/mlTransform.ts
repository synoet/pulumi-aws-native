// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Glue::MLTransform
 *
 * @deprecated MlTransform is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class MlTransform extends pulumi.CustomResource {
    /**
     * Get an existing MlTransform resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): MlTransform {
        pulumi.log.warn("MlTransform is deprecated: MlTransform is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new MlTransform(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:glue:MlTransform';

    /**
     * Returns true if the given object is an instance of MlTransform.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MlTransform {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MlTransform.__pulumiType;
    }

    public readonly description!: pulumi.Output<string | undefined>;
    public readonly glueVersion!: pulumi.Output<string | undefined>;
    public readonly inputRecordTables!: pulumi.Output<outputs.glue.MlTransformInputRecordTables>;
    public readonly maxCapacity!: pulumi.Output<number | undefined>;
    public readonly maxRetries!: pulumi.Output<number | undefined>;
    public readonly name!: pulumi.Output<string | undefined>;
    public readonly numberOfWorkers!: pulumi.Output<number | undefined>;
    public readonly role!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<any | undefined>;
    public readonly timeout!: pulumi.Output<number | undefined>;
    public readonly transformEncryption!: pulumi.Output<outputs.glue.MlTransformTransformEncryption | undefined>;
    public readonly transformParameters!: pulumi.Output<outputs.glue.MlTransformTransformParameters>;
    public readonly workerType!: pulumi.Output<string | undefined>;

    /**
     * Create a MlTransform resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated MlTransform is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: MlTransformArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("MlTransform is deprecated: MlTransform is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.inputRecordTables === undefined) && !opts.urn) {
                throw new Error("Missing required property 'inputRecordTables'");
            }
            if ((!args || args.role === undefined) && !opts.urn) {
                throw new Error("Missing required property 'role'");
            }
            if ((!args || args.transformParameters === undefined) && !opts.urn) {
                throw new Error("Missing required property 'transformParameters'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["glueVersion"] = args ? args.glueVersion : undefined;
            resourceInputs["inputRecordTables"] = args ? args.inputRecordTables : undefined;
            resourceInputs["maxCapacity"] = args ? args.maxCapacity : undefined;
            resourceInputs["maxRetries"] = args ? args.maxRetries : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["numberOfWorkers"] = args ? args.numberOfWorkers : undefined;
            resourceInputs["role"] = args ? args.role : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["timeout"] = args ? args.timeout : undefined;
            resourceInputs["transformEncryption"] = args ? args.transformEncryption : undefined;
            resourceInputs["transformParameters"] = args ? args.transformParameters : undefined;
            resourceInputs["workerType"] = args ? args.workerType : undefined;
        } else {
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["glueVersion"] = undefined /*out*/;
            resourceInputs["inputRecordTables"] = undefined /*out*/;
            resourceInputs["maxCapacity"] = undefined /*out*/;
            resourceInputs["maxRetries"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["numberOfWorkers"] = undefined /*out*/;
            resourceInputs["role"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["timeout"] = undefined /*out*/;
            resourceInputs["transformEncryption"] = undefined /*out*/;
            resourceInputs["transformParameters"] = undefined /*out*/;
            resourceInputs["workerType"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["inputRecordTables"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(MlTransform.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a MlTransform resource.
 */
export interface MlTransformArgs {
    description?: pulumi.Input<string>;
    glueVersion?: pulumi.Input<string>;
    inputRecordTables: pulumi.Input<inputs.glue.MlTransformInputRecordTablesArgs>;
    maxCapacity?: pulumi.Input<number>;
    maxRetries?: pulumi.Input<number>;
    name?: pulumi.Input<string>;
    numberOfWorkers?: pulumi.Input<number>;
    role: pulumi.Input<string>;
    tags?: any;
    timeout?: pulumi.Input<number>;
    transformEncryption?: pulumi.Input<inputs.glue.MlTransformTransformEncryptionArgs>;
    transformParameters: pulumi.Input<inputs.glue.MlTransformTransformParametersArgs>;
    workerType?: pulumi.Input<string>;
}
