// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iottwinmaker

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::IoTTwinMaker::Entity
type Entity struct {
	pulumi.CustomResourceState

	// The ARN of the entity.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// A map that sets information about a component type.
	Components pulumi.AnyOutput `pulumi:"components"`
	// The date and time when the entity was created.
	CreationDateTime pulumi.StringOutput `pulumi:"creationDateTime"`
	// The description of the entity.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The ID of the entity.
	EntityId pulumi.StringPtrOutput `pulumi:"entityId"`
	// The name of the entity.
	EntityName pulumi.StringOutput `pulumi:"entityName"`
	// A Boolean value that specifies whether the entity has child entities or not.
	HasChildEntities pulumi.BoolOutput `pulumi:"hasChildEntities"`
	// The ID of the parent entity.
	ParentEntityId pulumi.StringPtrOutput `pulumi:"parentEntityId"`
	// The current status of the entity.
	Status EntityStatusOutput `pulumi:"status"`
	// A key-value pair to associate with a resource.
	Tags pulumi.AnyOutput `pulumi:"tags"`
	// The last date and time when the entity was updated.
	UpdateDateTime pulumi.StringOutput `pulumi:"updateDateTime"`
	// The ID of the workspace.
	WorkspaceId pulumi.StringOutput `pulumi:"workspaceId"`
}

// NewEntity registers a new resource with the given unique name, arguments, and options.
func NewEntity(ctx *pulumi.Context,
	name string, args *EntityArgs, opts ...pulumi.ResourceOption) (*Entity, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.WorkspaceId == nil {
		return nil, errors.New("invalid value for required argument 'WorkspaceId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"entityId",
		"workspaceId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Entity
	err := ctx.RegisterResource("aws-native:iottwinmaker:Entity", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEntity gets an existing Entity resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEntity(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EntityState, opts ...pulumi.ResourceOption) (*Entity, error) {
	var resource Entity
	err := ctx.ReadResource("aws-native:iottwinmaker:Entity", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Entity resources.
type entityState struct {
}

type EntityState struct {
}

func (EntityState) ElementType() reflect.Type {
	return reflect.TypeOf((*entityState)(nil)).Elem()
}

type entityArgs struct {
	// A map that sets information about a component type.
	Components interface{} `pulumi:"components"`
	// The description of the entity.
	Description *string `pulumi:"description"`
	// The ID of the entity.
	EntityId *string `pulumi:"entityId"`
	// The name of the entity.
	EntityName *string `pulumi:"entityName"`
	// The ID of the parent entity.
	ParentEntityId *string `pulumi:"parentEntityId"`
	// A key-value pair to associate with a resource.
	Tags interface{} `pulumi:"tags"`
	// The ID of the workspace.
	WorkspaceId string `pulumi:"workspaceId"`
}

// The set of arguments for constructing a Entity resource.
type EntityArgs struct {
	// A map that sets information about a component type.
	Components pulumi.Input
	// The description of the entity.
	Description pulumi.StringPtrInput
	// The ID of the entity.
	EntityId pulumi.StringPtrInput
	// The name of the entity.
	EntityName pulumi.StringPtrInput
	// The ID of the parent entity.
	ParentEntityId pulumi.StringPtrInput
	// A key-value pair to associate with a resource.
	Tags pulumi.Input
	// The ID of the workspace.
	WorkspaceId pulumi.StringInput
}

func (EntityArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*entityArgs)(nil)).Elem()
}

type EntityInput interface {
	pulumi.Input

	ToEntityOutput() EntityOutput
	ToEntityOutputWithContext(ctx context.Context) EntityOutput
}

func (*Entity) ElementType() reflect.Type {
	return reflect.TypeOf((**Entity)(nil)).Elem()
}

func (i *Entity) ToEntityOutput() EntityOutput {
	return i.ToEntityOutputWithContext(context.Background())
}

func (i *Entity) ToEntityOutputWithContext(ctx context.Context) EntityOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EntityOutput)
}

type EntityOutput struct{ *pulumi.OutputState }

func (EntityOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Entity)(nil)).Elem()
}

func (o EntityOutput) ToEntityOutput() EntityOutput {
	return o
}

func (o EntityOutput) ToEntityOutputWithContext(ctx context.Context) EntityOutput {
	return o
}

// The ARN of the entity.
func (o EntityOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// A map that sets information about a component type.
func (o EntityOutput) Components() pulumi.AnyOutput {
	return o.ApplyT(func(v *Entity) pulumi.AnyOutput { return v.Components }).(pulumi.AnyOutput)
}

// The date and time when the entity was created.
func (o EntityOutput) CreationDateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.CreationDateTime }).(pulumi.StringOutput)
}

// The description of the entity.
func (o EntityOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The ID of the entity.
func (o EntityOutput) EntityId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringPtrOutput { return v.EntityId }).(pulumi.StringPtrOutput)
}

// The name of the entity.
func (o EntityOutput) EntityName() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.EntityName }).(pulumi.StringOutput)
}

// A Boolean value that specifies whether the entity has child entities or not.
func (o EntityOutput) HasChildEntities() pulumi.BoolOutput {
	return o.ApplyT(func(v *Entity) pulumi.BoolOutput { return v.HasChildEntities }).(pulumi.BoolOutput)
}

// The ID of the parent entity.
func (o EntityOutput) ParentEntityId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringPtrOutput { return v.ParentEntityId }).(pulumi.StringPtrOutput)
}

// The current status of the entity.
func (o EntityOutput) Status() EntityStatusOutput {
	return o.ApplyT(func(v *Entity) EntityStatusOutput { return v.Status }).(EntityStatusOutput)
}

// A key-value pair to associate with a resource.
func (o EntityOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v *Entity) pulumi.AnyOutput { return v.Tags }).(pulumi.AnyOutput)
}

// The last date and time when the entity was updated.
func (o EntityOutput) UpdateDateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.UpdateDateTime }).(pulumi.StringOutput)
}

// The ID of the workspace.
func (o EntityOutput) WorkspaceId() pulumi.StringOutput {
	return o.ApplyT(func(v *Entity) pulumi.StringOutput { return v.WorkspaceId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EntityInput)(nil)).Elem(), &Entity{})
	pulumi.RegisterOutputType(EntityOutput{})
}
