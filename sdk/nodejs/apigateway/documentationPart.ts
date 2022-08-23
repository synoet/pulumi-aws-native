// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ApiGateway::DocumentationPart
 */
export class DocumentationPart extends pulumi.CustomResource {
    /**
     * Get an existing DocumentationPart resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DocumentationPart {
        return new DocumentationPart(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:apigateway:DocumentationPart';

    /**
     * Returns true if the given object is an instance of DocumentationPart.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DocumentationPart {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DocumentationPart.__pulumiType;
    }

    /**
     * The identifier of the documentation Part.
     */
    public /*out*/ readonly documentationPartId!: pulumi.Output<string>;
    /**
     * The location of the API entity that the documentation applies to.
     */
    public readonly location!: pulumi.Output<outputs.apigateway.DocumentationPartLocation>;
    /**
     * The documentation content map of the targeted API entity.
     */
    public readonly properties!: pulumi.Output<string>;
    /**
     * Identifier of the targeted API entity
     */
    public readonly restApiId!: pulumi.Output<string>;

    /**
     * Create a DocumentationPart resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DocumentationPartArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.location === undefined) && !opts.urn) {
                throw new Error("Missing required property 'location'");
            }
            if ((!args || args.properties === undefined) && !opts.urn) {
                throw new Error("Missing required property 'properties'");
            }
            if ((!args || args.restApiId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'restApiId'");
            }
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["properties"] = args ? args.properties : undefined;
            resourceInputs["restApiId"] = args ? args.restApiId : undefined;
            resourceInputs["documentationPartId"] = undefined /*out*/;
        } else {
            resourceInputs["documentationPartId"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["properties"] = undefined /*out*/;
            resourceInputs["restApiId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(DocumentationPart.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DocumentationPart resource.
 */
export interface DocumentationPartArgs {
    /**
     * The location of the API entity that the documentation applies to.
     */
    location: pulumi.Input<inputs.apigateway.DocumentationPartLocationArgs>;
    /**
     * The documentation content map of the targeted API entity.
     */
    properties: pulumi.Input<string>;
    /**
     * Identifier of the targeted API entity
     */
    restApiId: pulumi.Input<string>;
}
